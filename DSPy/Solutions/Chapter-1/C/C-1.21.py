"""
Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs
those lines in reverse order (a user can indicate end of input by typing ctrl-D).
"""


lines = []
while True:
    try:
        user_input = input('Enter the line:')
        lines.append(user_input)
    except EOFError as e:
        print (e)
        print ("\nNow printing the lines in reverse order")
        break

for i in range(len(lines)-1,-1, -1):
    print(lines[i]) # or we can handle this with lines.pop()

