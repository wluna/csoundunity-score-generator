#!/usr/bin/env python3

# Initialization, open scores
import re
import random
from collections import defaultdict
score = open("bach.txt", "r")
staffOneSequence = open("staffOne.txt", "w")
staffTwoSequence = open("staffTwo.txt", "w")
print ("Launching Melody Parser")
# Separate arrays to store note information
noteDuration = list()
notePitches = list()
voices = list()
noteCycle = ["A", "B", "C", "D", "E", "F", "G"]
arrayLength = len(noteCycle)
noteDiff = [0, 1, -9, -7, -5, -4, -2]
currentNote = "A"
currentOctave = 0
currentAlter = 0
currentX = "0"
currentDuration = 1
frequency = 0
useful = False
x = 1.059460646483
lastStaff = 0
currentStaff = 1
newX = "1"
shortPlace = "00"
# F = {[(2)^1/12]^n} * 220 Hz
# F = {x^n} * 220 Hz
#variables for calculating frequency

#markovEvents = defaultdict(list)

def distA(note, octave):
	noteDist = 0
	newOct = int(octave)
	for i in range(arrayLength):
		if noteCycle[i] == note:
			noteDist = noteDiff[i]
	distance = (((newOct - 4) * 12) + noteDist)
	return distance

def pitchToFrequency(note, octave, alter):
	#1 how many half steps from A
	n = distA(note, octave)
	n = (n + alter)
	frequency = pow(x,n) * 220
	frequency = round(frequency, 2)
	return frequency

# Determines which voices exist in score; these will be read as instruments
# Places all note durations in a score into a list
# Counts number of notes in a score

for line in score:
# hoping to bypass later code with dictionary
	if "note default-x" in line:
		useful = False
		currentPlace = re.sub(r'<note default-x="', '', line)
		currentPlace = re.sub(r' ', '', currentPlace)
		#print (currentPlace)
		placeList = list(currentPlace)
		shortPlace = placeList[0] + placeList[1]
		#print (placeList)
		#firstPlace = int(placeList[0])
		newX = placeList[0] + placeList[1]
		#newX = int(newX)
		#print ("new X is " + newX)
		#print ("current x is: " + currentX)
		if (newX != currentX): #: OR the staffs are not the same
			#print ("novel note location")
			currentX = newX
			useful = True

	elif "step" in line:
		#strip markup
		currentNote = re.sub(r'step', '', line)
		currentNote = re.sub(r'<>', '', currentNote)
		currentNote = re.sub(r'</>', '', currentNote)
		#newScore.write()
		#place into list of all note durations, in sequence
		currentNote = currentNote.strip()
		currentAlter = 0

		#notePitches.append(newLine)
		#newScore.write((newLine) + ',')
	elif "alter" in line:
		currentAlter = re.sub(r'alter', '', line)
		currentAlter = re.sub(r'<>', '', currentAlter)
		currentAlter = re.sub(r'</>', '', currentAlter)
		currentAlter = currentAlter.strip()
		currentAlter = int(currentAlter)
		
	elif "octave" in line:
		currentOctave = re.sub(r'octave', '', line)
		currentOctave = re.sub(r'<>', '', currentOctave)
		currentOctave = re.sub(r'</>', '', currentOctave)
		currentOctave = currentOctave.strip()

	elif "duration" in line: 
		#strip markup
		currentDuration = re.sub(r'duration', '', line)
		currentDuration = re.sub(r'<>', '', currentDuration)
		currentDuration = re.sub(r'</>', '', currentDuration)
		#newScore.write()
		#place into list of all note durations, in sequence
		currentDuration = currentDuration.strip()
		#newLine = int(newLine)
		#noteDuration.append(newLine)
		#newScore.write((newLine) + '\n')
	elif "<staff>" in line:
		currentStaff = re.sub(r'staff', '', line)
		currentStaff = re.sub(r'<>', '', currentStaff)
		currentStaff = re.sub(r'</>', '', currentStaff)
		currentStaff = currentStaff.strip()
		currentStaff = int(currentStaff)
		#print ("The current staff is " + str(currentStaff))
		#print ("The last staff is " + str(lastStaff))
		if ((lastStaff != currentStaff) or (useful)):
			#print ("either the staff or the location is novel")
			frequency = pitchToFrequency(currentNote, currentOctave, currentAlter)
			frequency = str(frequency)
			#print ("frequency " + str(frequency) + " of duration " + str(currentDuration))
			#print ("is being placed into staff " + str(currentStaff)) 
			if (currentStaff == 1):
				staffOneSequence.write((frequency) + ', ')
				newDuration = (int(currentDuration) - 1)
				while (newDuration != 0): 
					staffOneSequence.write('0' + ', ')
					newDuration = (newDuration - 1)
			else:
				staffTwoSequence.write((frequency) + ', ')
				newDuration = (int(currentDuration) - 1)
				while (newDuration != 0): 
					staffTwoSequence.write('0' + ', ')
					newDuration = (newDuration - 1)

		lastStaff = currentStaff

#Ending procedure
#print ("There are " + (str(len(staffOneSequence))) + " notes in the staff one")
#print ("There are " + (str(len(staffTwoSequence))) + " notes in the staff two")
print ("End of script")
score.close()
staffOneSequence.close()
staffTwoSequence.close()



