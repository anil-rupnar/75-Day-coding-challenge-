"""
Problem statement: 
Shubham wrote a sequence of words the words. the words are written using the rule given below. thw sequence is concatenation o one or more words consisting of english letters.all latters in the first word are lowercase. for each of the subsequent words,the first letter is uppercase and rest of the latter are lowercase. you need to find the number of words in the string s. 
Input :
A single line of input that cantain the string S.

Output :
print the number of words in S.
"""
def count_words(s):
    # Initialize the count to 1, as the first word is always in lowercase
    word_count = 1
    
    # Iterate through each character in the string starting from the second character
    for i in range(1, len(s)):
        # Check if the current character is uppercase
        if s[i].isupper():
            # Increment the word count when an uppercase letter is found
            word_count += 1
    
    print(word_count)

s = input("Enter the string: ")

count_words(s)

