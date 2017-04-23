'''
MTspeller is a command line tool that helps its users practice American 
English spelling in an interactive way.

MTspeller: Copyright (c) 2016, ModarTensai (ModarTensai@gmail.com)
License: BSD 2-Clause (https://opensource.org/licenses/BSD-2-Clause)

For this tool to work, you have to have the following Python packages installed
(This was tested on the versions provided and Python 3.5.1 installed on Windows 10)

    PyEnchant==1.6.6
    PyDictionary==1.5.2
    Speech==0.5.2
	PyWin32 (For the corresponding version of python you have)
	
pip::

    pip install PyEnchant==1.6.6
    pip install PyDictionary==1.5.2
    pip install Speech==0.5.2

There was some little modefications made to the following files in order to work properly
Nothing will be missed up and you can always backup the files just in case:

    File: %PythonLocation%\Lib\site-packages\PyDictionary\Utils.py
        Line #5 changed from
            return BeautifulSoup(requests.get(url).text)
        To
            return BeautifulSoup(requests.get(url).text, 'html.parser')
	Reason
	    To rid of the warning from using BeautifulSoup4 without specifing default parser

    File: %PythonLocation%\Lib\site-packages\speech.py
        Line #59 changed from
            import _thread
        To
            import thread
        Line #157 changed from
            print prompt
        To
            print (prompt)
        Reason
            To make it run in Python 3
'''
help = '''
MTspeller V1.0, by ModarTensai <ModarTensai@gmail.com>

This package provides a tool to help its user practice American 
English spelling in an interactive way.

https://github.com/ModarTensai/MTspeller

    You have the following options to pick from:
	1. Type any sentence then hit enter 
				to hear it pronounced with all spelling mistakes highlighted
	2. Type ":" then any word of your choice 
				to see it in the dictionary (needs Internet connection)
	3. Type "$" then any shell command 
				to execute it ('help', 'cls' and 'exit' are common commands)
	4. Type "::" then any word of your choice 
				to suggest similarly spelled words
		
    Examples
	1. >>> I love playing witt my kids
	   >>> I love playing **** my kids
	2. >>> :wonderful
	   >>> Adjective
		   extraordinarily good or great; used especially as intensifiers
		   Synonyms
		   fantastic
		   remarkable
		   outstanding
		   awesome
		   magnificent
		   Antonyms
		   usual
		   tiny
		   unpleasant
		   typical
		   unremarkable
	3. >>> $cls
	   >>> [Windows console screen cleared]
	4. >>> ::wonderfl
	   >>> wonderful
	       wonder fl
	       wonderland
	       wonderer
	       wondering
	       wonderment
'''

import _thread
from os import system

#Spelling Checker
import enchant
endic = enchant.Dict('en_US')
check = endic.check
suggest = endic.suggest

#Pronouncer
from speech import say
#asynchronous version of say
asay = lambda text: _thread.start_new_thread(lambda x:say(x) , (text,))

#Dictionary
from PyDictionary import PyDictionary
dictionary = PyDictionary()
def define(word, e=False):
	meaning = None
	if check(word): meaning = dictionary.meaning(word)
	if meaning is None: print('No such word\n'); return
	for type, list in meaning.items():
		print(type)
		if not e and len(list)>3: list = list[:3]
		for sen in list:
			print('\t'+sen)
	synonym = dictionary.synonym(word)
	if synonym is not None:
		print('Synonyms')
		for syn in synonym:
			print('\t'+syn)
	antonym = dictionary.antonym(word)
	if antonym is not None:
		print('Antonyms')
		for ant in antonym:
			print('\t'+ant)
#asynchronous retrieval of definitions
adefine = lambda word: _thread.start_new_thread(lambda x:define(x) , (word,))
##############################################
	
if __name__ == '__main__':
	while True:
		print()
		str = input()
		
		if len(str)>0:
			#shell command
			if str[0]=='$':
				if str[1:]=='exit':
					break
				if str[1:]=='help':
					print(help)
				else: system(str[1:])
				
			#either define or suggest
			elif str[0]==':':
				#suggest
				if len(str)>2 and str[1]==':':
					str = str[2:]
					asay(str)
					list = suggest(str)
					if list is None:
						print('No available suggestions')
					else:
						for sug in list:
							print('\t'+sug)
					
				#define
				elif len(str)>1:
					asay(str[1:])
					adefine(str[1:])
					
			#discover spelling mistakes
			else:
				asay(str)
				for s in str.split(' '):
					s.replace(' ', '')
					if len(s) < 1: continue
					if check(s): 
						print(s, end=' ')
					else: print('*'*len(s), end=' ')
				print()