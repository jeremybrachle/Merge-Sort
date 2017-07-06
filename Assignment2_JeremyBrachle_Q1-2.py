#This program will implement merge sort
#Jeremy Brachle 46659942
#23 February 2017

#import necessary libraries
import sys
import time
import re

#create a list for containing the numbers
numbers = []

#get the command line argument
numberFile = sys.argv[1]

#open the file
readFile = open(numberFile, 'r')

#read into one variable
data = readFile.read()

#strip the \n characters and replace with space
stringNumbers = re.sub(r'\n', ' ', data)

#put the data into the list where entries are delimited by spaces (default character delimiter)
numbers = stringNumbers.split()

#turn characters into integers
numbers = map(int, numbers)

#merge sort function:
def mergeSort(values):
	#check to see if the length is more than one
	if len(values) > 1:
		#split into halves
		mid = len(values)/2
		#left half side is all numbers before the middle
		leftHalfSide = values[:mid]
		#right half side of all numbers after the middle
		rightHalfSide = values[mid:]

		#recursively call the merge sort function for the left and right sides (break down each side)
		mergeSort(leftHalfSide)
		mergeSort(rightHalfSide)

		#set up index counters:
		i=0
		j=0
		k=0
		
		#build back up in ascending order
		#loop through each half until equally sorted (or until one uneven half finishes)
		while i < len(leftHalfSide) and j < len(rightHalfSide):
			if leftHalfSide[i] < rightHalfSide[j]:
				values[k]=leftHalfSide[i]
				i=i+1
			else:
				values[k]=rightHalfSide[j]
				j=j+1
			k=k+1

		#finish left side
		while i < len(leftHalfSide):
			values[k]=leftHalfSide[i]
			i=i+1
			k=k+1

		#finish right side
		while j < len(rightHalfSide):
			values[k]=rightHalfSide[j]
			j=j+1
			k=k+1


#start the timer (multiply by 1000 to get milliseconds)
timeInitial = time.time() * 1000
#call the function by passing the array in
mergeSort(numbers)
#stop the timer
timeFinal = time.time() * 1000

#output the time it took to sort
print("Time to sort: %s milliseconds\n" % (timeFinal - timeInitial))
#output the sorted list
print numbers