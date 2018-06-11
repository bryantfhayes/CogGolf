import os, sys, re, json, random, string

#
# Abstract class for containing knowledge of a specific code challenge (e.g - ReverseString)
#
class Challenge(object):
    def __init__(self, name):
        self.name = name
        self.description = ""

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
# Class for Reverse String Challenge
#
class ReverseStringChallenge(Challenge):
  def __init__(self):
    Challenge.__init__(self, "ReverseString")
    self.input_args = self.random_word()
    self.description = '''An alphanumeric (CAPS only) string S, of length N, is passed in as a command 
line argument. Print to STDOUT that string sorted alphanumerically (ascending).

Contraints:
10 < N < 250

Input:
LUXZP65IPA2BR8MBBP2A

Output:
22568AABBBILMPPPRUXZ
    '''

  def random_word(self):
      lines = open('words.txt').read().splitlines()
      myline = random.choice(lines)
      return myline

  def expected_output(self):
    return self.input_args[::-1]

#
# Class for RomanToDec String Challenge
#
class RomanToDecChallenge(Challenge):
  def __init__(self):
      Challenge.__init__(self, "RomanToDec")
      self.N = 0
      self.coding = zip([1000,900,500,400,100,90,50,40,10,9,5,4,1], ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"])
      self.input_args = self.random_roman_string()
      self.description = '''Given a roman numeral string as a command line argument, print out the decimal equivelent.
The string will be given in UPPERCASE ascii, and the decimal value will be between 1 - 3999.

Input:
MMMDCCCLXXXVIII

Output:
3888
    '''

  def decToRoman(self, num):
    if num <= 0 or num >= 4000 or int(num) != num:
        raise ValueError('Input should be an integer between 1 and 3999')
    result = []
    for d, r in self.coding:
        while num >= d:
            result.append(r)
            num -= d
    return ''.join(result)

  def random_roman_string(self):
            self.N = random.randint(1, 3999)
            return self.decToRoman(self.N).upper()

  def expected_output(self):
      return str(self.N)

#
# Class for Sorting String Challenge
#
class SortStringChallenge(Challenge):
  def __init__(self):
      Challenge.__init__(self, "SortString")
      self.input_args = self.random_string()
      self.description = '''Given a string as a command line argument, sort the string and print it to stdout. 
Do NOT include a newline character.

Input:
HelloWorld

Output:
dlroWolleH
    '''

  def random_string(self):
            N = random.randint(10, 250)
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

  def expected_output(self):
      return ''.join(sorted(self.input_args))

#
# Class for Reverse String Challenge
#
class HelloWorldChallenge(Challenge):
  def __init__(self):
    Challenge.__init__(self, "HelloWorld")
    self.input_args = ""
    self.description = '''Print the string 'Hello World' to stdout.

Output:
Hello World
    '''

  def expected_output(self):
    return "Hello World"
