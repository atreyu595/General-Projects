#Simple python script that randomly capitalizes letters
#Has some underlying humor behind it's purpose and function
#Enjoy and feel free to use it :)

import random
from random import choice

#Accept input from user
string = input("Enter Text: ")

#print string, choice randomly selects letters from a string via string index "c"
#join these letters together to form sentence
print(''.join(choice((str.upper, str.lower))(c) for c in string))

