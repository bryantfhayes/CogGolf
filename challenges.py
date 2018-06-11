import os, sys, re, json, random, string

#
# Abstract class for containing knowledge of a specific code challenge (e.g - ReverseString)
#
class Challenge(object):
    def __init__(self, name):
        self.name = name

        # Init file structure
        if not os.path.isdir("challenges"):
        	os.mkdir("challenges")

       	if not os.path.isdir(os.path.join("challenges", self.name)):
       		os.mkdir(os.path.join("challenges", self.name))

       	if not os.path.isdir(os.path.join(os.path.join("challenges", self.name), "uploads")):
       		os.mkdir(os.path.join(os.path.join("challenges", self.name), "uploads"))

       	if not os.path.isdir(os.path.join(os.path.join("challenges", self.name), "compiled")):
       		os.mkdir(os.path.join(os.path.join("challenges", self.name), "compiled"))

       	self.upload_dir = os.path.join(os.path.join("challenges", self.name), "uploads")
       	self.compile_dir = os.path.join(os.path.join("challenges", self.name), "compiled")

    def expected_output(self):
        pass

#
# Class for Sorting String Challenge
#
class SortStringChallenge(Challenge):
	def __init__(self):
	    Challenge.__init__(self, "SortString")
	    self.input_args = self.random_string()

	def random_string(self):
            N = random.randint(10, 250)
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

	def expected_output(self):
	    return ''.join(sorted(self.input_args))

#
# Class for Reverse String Challenge
#
class ReverseStringChallenge(Challenge):
	def __init__(self):
		Challenge.__init__(self, "ReverseString")
		self.input_args = self.random_word()

	def random_word(self):
	    lines = open('words.txt').read().splitlines()
	    myline = random.choice(lines)
	    return myline

	def expected_output(self):
		return self.input_args[::-1]

#
# Class for Reverse String Challenge
#
class HelloWorldChallenge(Challenge):
	def __init__(self):
		Challenge.__init__(self, "HelloWorld")
		self.input_args = ""

	def expected_output(self):
		return "Hello World"
