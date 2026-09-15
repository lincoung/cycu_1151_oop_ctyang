#exercis 9.15.3
#Python provides a built-in function called reversed that takes as an argument a sequence of elements – like a list or string – and returns a reversed object that contains the elements in reverse order.

arg = reversed('parrot')

print (arg)
#The reversed object is an iterator, which means that it can be used in a for loop like this.
#If you want the reversed elements in a list, you can use the list function.

arg = list(reversed('parrot'))

print (arg)
#['t', 'o', 'r', 'r', 'a', 'p']
#Or if you want them in a string, you can use the join method.

arg = ''.join(reversed('parrot'))
'torrap'
#So we can write a function that reverses a word like this.

def reverse_word(word):
    return ''.join(reversed(word))


def is_palindrome(word):
    return word == reverse_word(word)

#A palindrome is a word that is spelled the same backward and forward, like “noon” and “rotator”. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise.
#You can use the following loop to find all of the palindromes in the word list with at least 7 letters.
word_list = ['noon', 'redivider', 'deified', 'civic', 'radar', 'level', 'rotor', 'kayak', 'reviver', 'racecar', 'madam', 'refer']   

for word in word_list:
    if len(word) >= 7 and is_palindrome(word):
        print(word)