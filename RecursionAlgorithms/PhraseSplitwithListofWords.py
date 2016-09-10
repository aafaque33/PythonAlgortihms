# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

# **Input: **
# word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])

# **Output: **
# ['i', 'love', 'dogs', 'John']


# Check if the phrase can be splitted into list of words provided using recursion

def word_split(phrase,list_of_words,splitstring=[]):
    
    if len(phrase) == 0:
        return splitstring
    
    for words in list_of_words:
        
        if (phrase.find(words,0,len(words)) != -1):
            splitstring.append(words)
            word_split(phrase[len(words):],list_of_words,splitstring)
            
    return splitstring


splitstr = word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])

print(splitstr)

