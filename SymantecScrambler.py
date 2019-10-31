import argparse
import art 

python script
def main():
	#Create Parser Obj to get input arguments
	parser = argparse.ArgumentParser(description='Yet Another Web Fuzzing Tool Designed to Brute Force Directories')
	parser.add_argument('-f','--file',  action="store", dest="fileName", help='Takes in the payload you would like scrambled')
	parser.add_argument('-t', '--type', action="store", dest="payloadType", nargs='?', const=1, type=string, default='psh', help="Takes in the expected payload type")
	parser.add_argument('-o','--output',  action="store", dest="outputFileName", help='File to output results to')
	parser.add_argument('--verbose', action="store_true", help='Print Verbose Output')
	parser.add_argument('--version', action='version', version='%(prog)s 1.1')

	#Check and Ensure Proper Arguments were passed.  If not, displays help menu
	if len(sys.argv[1:]) == 0:
		printAsciiTitle()
		parser.print_help()
		parser.exit()
	#Start the Scrambling
	inputs = parser.parse_args()
	
	if inputs.payloadType == 'psh':
		printAsciiEgg()
		cleanFile = open(fileName,"r")
		cleanContent = cleanFile.read()
		

		scrambledData = null
		if inputs.outputFileName == True:
			scrambledFile = open(outputFileName,"w+")
			scrambledFile.write(scrambledData)
		else:
			print(scrambledData)
def printAsciiTitle():
	tprint("Symantec Scrambler",font="graffiti")
	
if __name__ == "__main__":
	main()
