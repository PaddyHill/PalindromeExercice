#function to check if a Word is a palindrome
def is_palindrome(palindrome_word):
    #Check the word forward and backward
    if palindrome_word == palindrome_word[::-1]:
        #if its a palindrome output true
        return True

    else:
        #if not output false
        return False
