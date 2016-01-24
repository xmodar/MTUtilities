mtspeller:  Python program to help you practice spelling in English
========================================

This package provides a tool to help its user practice American 
English spelling in an interactive way.


What is MTspeller?
--------------------

MTspeller is an interactive console that let you type anything in your mind and once
you hit enter it pronounce the sentence you wrote and highlight any spelling mistakes
you made. You can, of course, try again as many times as you want and you can even
make it suggest to you the correct spelling. It ships, also, with a dictionary to define
words and gives synonyms and antonyms for the world; if exist. It needs Internet
connection to work properly.


How to install it?
------------------

You have to have the following Python packages installed in order to run this software
(The package was tested on the versions provided and Python 3.5.1 installed on Windows 10)

	PyEnchant==1.6.6
	PyDictionary==1.5.2
	Speech==0.5.2
	
pip::

    pip install PyEnchant==1.6.6
    pip install PyDictionary==1.5.2
    pip install Speech==0.5.2

There was some little modefications made to the following files in order to work properly:

	File: %PythonLocation%\Lib\site-packages\PyDictionary\Utils.py
		Line #5 changed from
			return BeautifulSoup(requests.get(url).text)
		To
			return BeautifulSoup(requests.get(url).text, 'html.parser')
		Reason
			To get rid of an unplasant warning of using BeautifulSoup4 without specifing default parser

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
			
			
How do I use it?
-----------------

Once the software is installed and everything is in place, you can use the MTspeller as follows:

	You have the following options to pick from:
		1. Type any sentence then hit enter: to hear it pronounced with all spelling mistakes highlighted
		2. Type ":" then any word of your choice to see it in the dictionary (needs Internet connection)
		3. Type "$" then any shell command to execute it ('cls' is common to clear screen in Windows)
		4. Type "::" then any word of your choice to suggest similarly spelled words
		
	Examples
		1. >>> I love playing witt my kids
			>>> I love playing *** my kids
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
			>>> 		wonderful
							wonder fl
							wonderland
							wonderer
							wondering
							wonderment


Who is responsible for this?
------------------------------

This is a simple software I coded for my personal use to prepare for TOEFL and GRE exams
and strengthen my English spelling skills. It is intended for personal use and I hope somebody
will benefit from it like I did.

Bugs can be filed on the project's github page:

    https://github.com/

Comments, suggestions, other feedback can be emailed to me directly:

    ModarTensai@gmail.com