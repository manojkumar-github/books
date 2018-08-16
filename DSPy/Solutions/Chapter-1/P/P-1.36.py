"""
Write a Python program that inputs a list of words, separated by white- space, and outputs how many times each word
appears in the list. You need not worry about efficiency at this point, however, as this topic is something that will
be addressed later in this book.
"""

ip_lst = input('Enter the list of words seperated by whitespaces:')
ip_lst = ip_lst.split()

word_count_table = {}
for word in ip_lst:
    if word in word_count_table.keys():
        word_count_table[word]+=1
    else:
        word_count_table[word] = 1

print (word_count_table)
