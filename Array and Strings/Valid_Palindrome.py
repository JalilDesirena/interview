

s = "A man a plan, a canal Panama"

a_string = 'Was it a car or a cat I saw'
#1.- clean the spaces and comas
#2.- convert chars into lowercase
#3.- Convert into list 
#4.- Reverst the list
#5.- Compare

def isPalindrome( s:str) -> bool:
    filtered_chars = filter(lambda ch: ch.isalnum(), s)
    lowercasefilter_chars = map(lambda ch: ch.lower(), filtered_chars)
    fstring= list(lowercasefilter_chars)
    Rstring= fstring[::-1]
    return fstring == Rstring
 
 
def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]

print(palindrome(a_string))
print(isPalindrome(s))  