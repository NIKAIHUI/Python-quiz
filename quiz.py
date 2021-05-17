# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?



blanks= ['___1___', '___2___', '___3___', '___4___']

message = '''\nWelcome to participate in Python knowledge check quiz.
There are three different modes according to your Python theory knowledge use, each knowledge level contains four quizzes.
'''

basics = '''\nPython is currently the most widely used multi-purpose, high-level ___1___ language.
Python allows programming in Object-Oriented and ___2___ paradigms.
Python programs generally are smaller than other programming languages like Java.  It was designed with an emphasis on code readability, 
and its ___3___ allows programmers to express their concepts in fewer lines of code.
Before we start Python programming, we need to have an ___4___ to interpret and run our programs.
'''
basics_answers = ['programming', 'procedural', 'syntax', 'interpreter']

concepts = '''\nA ___1___ is a user-defined prototype for an object that defines a set of attributes that
characterise any object of the ___1___. The attributes are data members and ___2___, accessed via dot notation.
A ___2___ is a special kind of function that is defined in a ___1___ definition.
A ___3___ a special ___2___ that is automatically invoked right after a new object is created. The ___3___ 
___2___, __init__() is usually used to set up the initial attribute values of an object.
One of the key elements of OOP is ___4___, which allows you to base a new class on an existing one. By 
doing so, the new class automatically gets (or inherits) all of the methods and attributes of the existing 
class.
'''
concepts_answers = ["class", "method", "constructor", "inheritance"]

advanced = '''\nIn an object-oriented program like Python, you can restrict access to methods and variables.
This can prevent data from being modified by accident and is known as ___1___.
The process of using an operator or function in different ways for different data input is called ___2___.
In practical terms, ___2___ means that if class B inherits from class A, it doesn't have to inherit everything
about class A; it can do some of the things that class A does differently.
In object-oriented programming theory, ___3___ is a technique of managing complexity of computer systems.
It works by establishing a level of complexity in which a person interacts with the system, suppressing the 
more complex details below the current level.
It might sound that ___1___ is similar to ___3___. That's because they're closely related as ___1___ is a 
principal of ___3___. In simpler terms, ___3___ saves you from worrying about the details while ___1___ hides
the details from you.
The process of defining something in terms of itself is called ___4___. We know that in Python, a function 
can call other functions. It is even possible for the function to call itself. These type of construct are 
termed as recursive functions.
'''
advanced_answers = ["encapsulation", "polymorphism", "abstraction", "recursion"]


def quiz_mode():
	'''Input - prompts the user for their request of quiz mode and returns corresponding mode.'''
	
	print('Please choose a mode to check your Python understanding:  Basics  Concepts  Advanced')
	modes = ['basics', 'concepts', 'advanced']
	mode = ''

	while mode not in modes:
		mode = input('Choose a level: ').lower()
		if mode == 'basics':
			return basics, basics_answers
		elif mode == 'concepts':
			return concepts, concepts_answers
		elif mode == 'advanced':
			return advanced, advanced_answers
		else:
			print('Invalid input')


def user_answer(word):
	'''Input - takes the answer from the user as input and then processes it to check if the answer
	coincides with the correct answer.'''
	user_answer_input = input(f'\nEnter your answer for {word} : ').lower()
	return user_answer_input
	

def main():
	'''function to make the game work and return the result'''
	i = 0 #i stands for the iteration within the blanks
	print(message)
	user_mode, answer = quiz_mode()
	while i < len(blanks):
		#print(user_mode)
		guess_answer = user_answer(blanks[i])
		if guess_answer == answer[i]:
			print('\nCorrect!')
			user_mode = user_mode.replace(blanks[i], guess_answer)
			i += 1
		else:
			print('\nSorry, try again.')
	print('Congratulations!')
	print(user_mode)
	input('Press the enter key to exit.')
			

main()