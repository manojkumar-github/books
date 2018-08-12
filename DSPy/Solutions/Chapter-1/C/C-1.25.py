"""
Write a short Python function that takes astrings,representing a sentence, and returns a copy of the string with all
punctuation
removed. For example, if given the string "Let's try, Mike.", this function would return "Lets try Mike".
"""

def remove_punct(sentence):
    new_sentence = []
    for i in range(len(sentence)):
        if sentence[i].isalnum() or sentence[i]==' ':
            new_sentence.append(sentence[i])
    return ''.join(new_sentence)

print (remove_punct("Let's try, Mike."))
print (remove_punct(""))

