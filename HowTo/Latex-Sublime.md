# Latex on SublimeText 3

This is a guide to work with latex in SublimeText 3 on Ubuntu 14.04 LTS:

 * First of all, you have to have [SublimeText 3](https://www.sublimetext.com).
 * Then, install [Package Control](https://packagecontrol.io/installation) on Sublime.
 * Click `Ctrl+Shift+P` in Sublime and pick "Package Control: Install Package".
 * Then, pick "LaTeXTools".
 * Now, in the terminal `Ctr+Alt+T`
```sh
sudo apt-get install ghostscript
sudo apt-get install imagemagick
sudo apt-get install texlive
sudo apt-get install latexmk
sudo apt-get install texlive-xetex
sudo apt-get install biber
sudo apt-get install texlive-latex-extra
```

Check that you have everything you need by clicking `Ctrl+Shift+P` in Sublime and pick "LaTeXTools: Check System".