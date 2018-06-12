import os, json, time, copy, random, re, six
from subprocess import Popen, call, PIPE
from database import SFDatabase
import challenges
from shutil import copyfile

# FOR_EACH_TEST: Add new challenge string
REVERSE_STRING_CHALLENGE = "ReverseString"
HELLO_WORLD_CHALLENGE = "HelloWorld"
SORT_STRING_CHALLENGE = "SortString"
ROMAN_TO_DECIMAL_CHALLENGE = "RomanToDec"

#
# Submission object created when code is submitted for a challenge
#
class Submission(object):
    def __init__(self, name, path_to_file, challenge):
        self.allowed_extensions = set(["c"])
        self.path_to_file = path_to_file
        self.challenge = challenge
        self.time = str(time.time()).split('.')[0]
        self.name = name
        self.valid = False

        # Copy file to the challenge directory and rename to timestamp
        self.src_file = os.path.join(challenge.upload_dir, (self.time + ".c"))
        self.out_file = os.path.join(challenge.compile_dir, (self.time + ".o"))
        copyfile(self.path_to_file, self.src_file)

        # JSON Serializable Parameters
        self.data = {}
        self.data["name"] = self.name
        self.data["input_args"] = self.challenge.input_args
        self.data["expected_output"] = self.challenge.expected_output()
        self.data["src_file"] = self.src_file
        self.data["out_file"] = self.out_file
        self.data["count"] = self.character_count()
        self.data["stderr"] = ""
        self.data["stdout"] = ""
        self.data["return_status"] = ""
        self.data["compiled"] = False
        self.data["compilation_output"] = ""
        self.data["compilation_error"] = ""
        self.data["compilation_status"] = ""
        self.data["time"] = self.time
        self.data["challenge"] = self.challenge.name

        self.data["compiled"] = self.compile()
        print("Compilation {}".format("Successful" if self.data["compiled"] else "Failed"))

        # Check if test passes criteria!
        self.data["iteration"] = 0
        passed = True
        for i in xrange(0, 100):
            self.data["iteration"] = i
            self.challenge.reload()
            self.data["valid"] = self.validate()
            if self.data["valid"] == False:
                passed = False
                break

        self.valid = passed

        print("Solution is {}".format("VALID" if passed else "INVALID"))

    def validate(self):
        ''' Run and then determine if the stdout matches what the challenge wants '''
        if not self.file_is_valid():
            return False

        self.run()
        
        if self.data["compiled"] == False:
            return False

        if self.data["stdout"] == self.challenge.expected_output():
            return True
        else:
            return False

    def character_count(self):
        ''' Count the number of non-whitespace characters in a file '''
        with open(self.path_to_file, 'r') as fp:
            text = fp.read()
        return len(text) - text.count('\n') - text.count('\r') - text.count(' ') - text.count('\t')

    def file_is_valid(self):
        ''' Check to see if submitted file is valid '''
        is_valid = ('.' in self.src_file) and (self.src_file.split('.')[-1].lower() in self.allowed_extensions)
        return is_valid

    def getData(self):
        ''' Return dictionary object representation of submission '''
        return self.data

    def compile(self):
        ''' Compile submitted code and return status '''
        p = Popen(["gcc", self.src_file, "-o", self.out_file], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.data["compilation_output"], self.data["compilation_error"] = p.communicate()
        self.data["compilation_status"] = p.returncode
        return False if p.returncode else True

    def run(self):
        ''' Run compiled code and return the Return Value. '''
        p = Popen([self.out_file + " " + self.challenge.input_args], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.data["stdout"], self.data["stderr"] = p.communicate()
        self.data["return_status"] = p.returncode
        return False if p.returncode else True

#
# Main class for controlling application
#
class CogGolf(object):
    def __init__(self):
        self.rel_database_path = "data.json"
        self.data = SFDatabase(self.rel_database_path)

        # FOR_EACH_TEST: Enable challenges and supply challenge strings
        self.data.setObjectForPath("challenges", { REVERSE_STRING_CHALLENGE : True, HELLO_WORLD_CHALLENGE : True, SORT_STRING_CHALLENGE : True, ROMAN_TO_DECIMAL_CHALLENGE : True })

        # Initialize challenges and load submissions
        self.challenges = {}
        self._challenges = self.data.getObjectForPath("challenges")
        for challenge in self._challenges:
            self.challenges[challenge] = self.challenge_obj_for_name(challenge)

        self.submissions = {}

    def challenge_obj_for_name(self, challenge_name):
        # FOR_EACH_TEST: Add section to get challenge obj from string
        if challenge_name == REVERSE_STRING_CHALLENGE:
            return challenges.ReverseStringChallenge()
        elif challenge_name == HELLO_WORLD_CHALLENGE:
            return challenges.HelloWorldChallenge()
        elif challenge_name == SORT_STRING_CHALLENGE:
            return challenges.SortStringChallenge()
        elif challenge_name == ROMAN_TO_DECIMAL_CHALLENGE:
            return challenges.RomanToDecChallenge()


    def get_submissions_for_challenge(self, challenge_name):
        ''' Return a list of submissions for specified challenge '''
        if self.data.getObjectForPath("submissions") == None:
            return []

        submissions = []
        for key, sub in six.iteritems(self.data.getObjectForPath("submissions")):
            if sub["challenge"].lower() == challenge_name.lower():
                submissions.append(sub)
        return submissions

    def new_submission(self, name, path_to_file, challenge_name):
        ''' Create a new Submission object and submit '''
        if challenge_name not in self.challenges:
            print("ERROR: Invalid Challenge")
            return False

        submission = Submission(name, path_to_file, self.challenge_obj_for_name(challenge_name))
        self.submissions[submission.time] = submission
        
        # Only save valid submissions
        if submission.valid:
            self.data.setObjectForPath("submissions/{}".format(submission.time), submission.getData())

        return submission






