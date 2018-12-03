#!/usr/bin/env python3

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print()
	equals_string = '=========='
	print(equals_string,' REVERSE ',equals_string)
	reverse1 = 'reverse'
	reverse2 = 'revature'
	reverse3 = 'gnitset'
	reverse4 = ''
	print(reverse1,'   ',reverse(reverse1))
	print(reverse2,'   ',reverse(reverse2))
	print(reverse3,'   ',reverse(reverse3))
	print('Empty string:',reverse4,'  reversed:',reverse(reverse4))

	print()
	print(equals_string,' ACRONYM ',equals_string)
	acronym1 = 'Relational Database Management System'
	acronym2 = 'One'
	acronym3 = ''
	acronym4 = 'Complementary Metal-Oxide semiconductor'
	print(acronym1,'   ', acronym(acronym1))
	print(acronym2,'   ', acronym(acronym2))
	print(acronym3,'   ', acronym(acronym3))
	print(acronym4,'   ', acronym(acronym4))

	print()
	print(equals_string,' WHICH TRIANGLE ',equals_string)
	print('20, 20, 20   ', whichTriangle(20,20,20))
	print('20, 15, 10   ', whichTriangle(20,15,10))
	print('20, 20, 15   ', whichTriangle(20,20,15))
	print('20, 15, 20   ', whichTriangle(20,15,20))
	print('15, 20, 20   ', whichTriangle(15,20,20))

	print()
	print(equals_string,' SCRABBLE ',equals_string)
	print('f   ',scrabble('f'))
	print('zoo ',scrabble('zoo'))
	print('street   ',scrabble('street'))
	print('quirky   ',scrabble('quirky'))
	print('OxyphenButazone  ',scrabble('OxyphenButazone'))

	print()
	print(equals_string,' ARMSTRONG ',equals_string)
	print('0   ',armstrong(0))
	print('9   ',armstrong(9))
	print('10  ',armstrong(10))
	print('153  ',armstrong(153))
	print('100  ',armstrong(100))
	print('9474  ',armstrong(9474))

	print()
	print(equals_string,' PRIME FACTORS ',equals_string)
	print('2:',primeFactors(2))
	print('9:',primeFactors(9))
	print('8:',primeFactors(8))
	print('12:',primeFactors(12))
	print('901255:',primeFactors(901255))

	print()
	print(equals_string,' PANGRAM ',equals_string)
	print('Empty string:',pangram(''))
	alphaLowCas = 'abcdefghijklmnopqrstuvwxyz'
	print(alphaLowCas,': ',pangram('abcdefghijklmnopqrstuvwxyz'))
	brownFox = 'the quick brown fox jumps over the lazy dog'
	print(brownFox,': ',pangram(brownFox))
	missingX = 'a quick movement of the enemy will jeopardize five gunboats'
	print(missingX,': ',pangram(missingX))
	missingAn = 'five boxing wizards jump quickly at it'
	print(missingAn,': ',pangram(missingAn))



'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	return string[::-1]

'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	if len(phrase) < 1:
		return 'none'
	acro = phrase[0]
	for index in range(len(phrase)):
		if(phrase[index] == ' ' or phrase[index] == '-'):
			acro+=phrase[index+1]
	return acro.upper()

'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	if(sideOne == sideTwo and sideOne == sideThree):
		return 'equilateral'
	elif(sideOne!=sideTwo and sideOne!=sideThree and sideTwo!=sideThree):
		return 'scalene'
	else:
		return 'isosceles'
		

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	score = 0
	for w in word:
		w = w.lower()
		if w=='a' or w=='e' or w=='i' or w=='o' or w=='u' or w=='l' or w=='n' or w=='r' or w=='s' or w=='t':
			score+=1
		elif w=='d' or w=='g':
			score+=2
		elif w=='b' or w=='c' or w=='m' or w=='p':
			score+=3
		elif w=='f' or w=='h' or w=='v' or w=='w' or w=='y':
			score+=4
		elif w=='k':
			score+=5
		elif w=='j' or w=='x':
			score+=8
		elif w=='q' or w=='z':
			score+=10
		else:
			score+=0
	return score

'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
	temp = number
	power = 0
	while temp > 0:
		power+=1
		temp//=10
	
	armstrong = 0
	temp = number
	while temp > 0:
		armstrong += pow(temp%10,power)
		temp = temp - temp%10
		temp = temp//10
	result = False
	if(number == armstrong):
		result = True
	return result

'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):
	factors = []
	index = 2
	while index <= number:
		if number%index==0:
			factors.append(index)
			number/=index
		else:
			index+=1
	return factors

'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
	result = True
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	alphabet = set(alpha)
	if len(sentence) > 0:
		for s in sentence:
			if s.isalpha():
				if s in alphabet:
					alphabet.remove(s)
		if len(alphabet) > 0:
			result = False
	return result

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
#def sort(numbers):

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
#def rotate(key, string):

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
#def evenAndOdds():

if __name__ == "__main__":
	main()
