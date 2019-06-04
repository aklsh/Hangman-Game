########################################################################
# Done By: Akilesh Kannan
# Version: v1.0
# Last Updated: Jun 03, 2019
########################################################################

import random
from os import system
import linecache as lc

#to print the elements of list without the annoying brackets and quotes
def printlist(guess,char):	
	for x in guess:
		print(x,end=char)

#to update the guess-word of the person, if needed after every letter guessed
def changeguess(guess,guessletter,word):	
	positions=[]

	for x in range(len(word)):
		if guessletter==word[x]:
			positions.append(x)
	for y in positions:
		guess[y] = guessletter

	return guess

#to check if the user's current guess is the actual answer
def checkguess(guess,word):	
	for x in range(len(word)):
		if guess[x]!=word[x]:
			return 1
	return 0

#to find out the number of lines in the file containing the words
num_lines = 0
with open('words.txt', 'rt') as f:
    for line in f:
        num_lines += 1

f=open('words.txt', 'rt')

#dictionary for the hangman word
hangmanword={0:'',1:'H',2:'H-A',3:'H-A-N',4:'H-A-N-G',5:'H-A-N-G-M',6:'H-A-N-G-M-A',7:'H-A-N-G-M-A-N'}

#initial screen
system('clear')
print("\t\t\t\tHANGMAN  -  A WORD GAME\t\t\t\t")
print("\t\t\tRULES:\n\t\t\tEnter w if you want to guess the whole word\n\t\t\tEnter l if you want to guess a letter that you think is present in the word.")
print("\n\t\t\t\tPress y to start")

cont=str(input())

while cont=='y':

	system('clear')

	wordnum=random.randint(1,num_lines)	#getting a random line number from the file
	wordtemp=lc.getline('words.txt',wordnum) 	#storing the required line, which contains both word and it's hint

	position=1

	#storing the word and hint in two separate variables
	while position<len(wordtemp):
		
		if wordtemp[position-1] != ":" :
			position+=1
		else:
			break

	word=wordtemp[0:position-1]
	meaning=wordtemp[position:len(wordtemp)-1]
	
	#Printing the word and hint
	print("The word is: ",end="")

	for x in range(len(word)):
		print("_",end="")
	print("")

	print("Hint to the word:",meaning)

	warning=0		#initialising warnings to 0

	guess=[]
	allguess=[]
	for x in range(len(word)):				#initialising word to ______ of required length
		guess.append('_')			

	while warning<8:
		
		print("\nEnter w if you want to guess the word and l if you want to guess a letter: ", end='')
		char=str(input())

		if char=='w':
			
			print("Enter the word (in smallcase letters only): ", end='')
			guessword=str(input())
			
			if guessword==word:		#check if guess is right answer
				
				print("\nThat is the right answer! You have won!!\n\t\t\t\t\tGame Over.")
				break
			
			else:
				
				if guessword  not in allguess:		#check if user already guessed it.

					allguess.append(guessword)
					warning+=1
					print("\nSorry, you have guessed it wrong. Your guess is now: ",end='')
					printlist(guess,'')
					print(".\nYour Hangman is now at", hangmanword[warning])
				
				else:
					
					print("\nYou had already guessed that word. Here is what you have guessed so far:\n")
					printlist(allguess,' ')
					print('\n')

				if warning==7:
					
					print("\n\t\t\t\t\tGame over.\n\t\t\t\tThe correct answer was:",word)
					break

		elif char=='l':
			
			print("Enter the letter that you think is present in the word (in smallcase only): ",end='')
			guessletter=str(input())
			
			if guessletter in word:
				
				if guessletter not in allguess:

					allguess.append(guessletter)
					print("\nYour guess was correct! That letter is indeed present in the word!")
					guess = changeguess(guess,guessletter,word)
					
					if checkguess(guess,word)==0:
						
						print("\t\t\t\t\tYay! You have found the word. The word is:", word)
						print("\t\t\t\t\tGame over")
						break
						
					else:
						
						print("\nYour guess is now: ",end='')
						printlist(guess,'')
						print(".\nYour Hangman is now at", hangmanword[warning])

				
				else:
					
					print("\nYou had already guessed that letter. Here is what you have guessed so far:\n")
					printlist(allguess,' ')
					print('\n')

			else:

				warning+=1
				
				if guessletter not in allguess:
					allguess.append(guessletter)
				
				else:
					
					print("\nYou had already guessed that letter. Here is what you have guessed so far:\n")
					printlist(allguess,' ')
					print('\n')

				print("\nYour guess was wrong.\nYour guess is now: ",end='')
				printlist(guess,'')
				print(".\nYour Hangman is now at", hangmanword[warning])

				if warning==7:
					print("\n\t\t\t\t\tGame over.\n\t\t\t\tThe correct answer was:",word)
					break
	
	print("\nDo you want to continue the game with another word? Enter y for yes and any other character on the keyboard for no")
	cont=str(input())
	system('clear')