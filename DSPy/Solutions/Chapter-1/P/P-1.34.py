"""
A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program
that will write out the following sentence one hundred times: “I will never spam my friends again.” Your program
should number each of the sentences and it should make eight different random-looking typos.
"""
import random
def punishment_100_times(n, sentence="I will never spam my friends again."):
    for i in range(1, n+1):
        if i % 12 == 0 and i>1:
            words = sentence.split()
            random_index = random.randint(0, len(words)-1)
            l = list(words[random_index])
            random.shuffle(l)
            words[random_index] = ''.join(l)
            print (i, ' '.join(words))
        else:
            print (i, sentence)

if __name__ == "__main__":
    punishment_100_times(100)