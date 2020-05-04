"""
To run this script:
	python EvenOdd.py

In order to pass the autograder your function should
return a list of even numbers given any list of integers.
If you run the above script, a correct function should return:

Even numbers are [2, 4]

What topics have you found it hard to understand? heuristics searches: including A*, greedy search
What topics are you most looking forward to? currently learning more about heursitics, and anything about AI in general
number of hours you spent on this assignment: 1 hour to do the whole assignment and 15 minutes to set up python
"""

def getEvenNumbers(numbers):
	evens = []
	"*** Add your code in here ***"
	for i in numbers:
		if i % 2 == 0:
			evens.append(i)


	return evens


if __name__ == '__main__':
	myList = [1, 2, 3, 4, 5]
	print("Even numbers are {}".format(getEvenNumbers(myList)))