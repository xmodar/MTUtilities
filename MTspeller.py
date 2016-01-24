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
				system(str[1:])
				
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