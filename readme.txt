v. 01    *shrug*

Whew.  Learned about the OS module, learned about shutil module, learned about try/except blocks.  Learned how to shorten up the code with .endswith, and having that be a tuple.  

Please, forget about the "else:" block here, because I realize that will always print out "Nothing To Do".  Also I realize that the labels have to be cleared before printing something else to them, probably with another label.  

My thinking was to create a cyclical motion through all of the files that it had moved.  Kind of like Windows did back in the day.   I guess Linux did it too.   *shrug*   But that's a problem we can deal with tomorrow.

 v. 02, I guess?

I realize that it only looks like I added an If/Else statement and a new variable called "moved_files", but it was harder than I expected.  First off, I had to remove the "Nothing to do!" statement from the for loop.   It was running over and over again, for everything that wasn't what I expected.   Then, I had to have some way to find out if the program did anything.   Easy way :  Add another variable called moved_files, have it increment, then check it against zero.

It was a lot harder than it looks.

Well, for me, at least.   

v .03  

I finally added code that would take in arguments (i, in this case), and put them out to the screen in the order in which they appeared.  Still have got to implement a feature that will delete the previous Label.  In other words, the one label "Not gonna get us.opus" is shorter than "Simon and Garfunkel - America.opus", so, then you will end up with "Not gonna get us.opus - America.opus".   Something like that.

And the buttons and the text aren't centered, but that's prettifying.  


