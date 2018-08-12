"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

def get_vowel_count(astring):
    cnt = 0
    for char in astring:
        if char in 'AEIOUaeiou':
            cnt +=1
    return cnt


print (get_vowel_count('Randomization'))
print (get_vowel_count(''))
