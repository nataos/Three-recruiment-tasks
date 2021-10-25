#task 1
N = input('Wprowadź liczbę')
def reversed_number(N):
    if int(N) > 0:
        reverse = int(N[::-1])
    else:
        N = N[1:]
        reverse = -(int(N[::-1]))

    if (-2147483648 > reverse) or (reverse > 2147483647):
        return 0
    else:
        return reverse

def test_reversed_number():
    N = '456'
    reverse = reversed_number(N)
    assert reverse == 654

print(test_reversed_number())
#print(reversed_number())

#task 2
list_of_numbers = [[],[], ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]
number = input('Wprowadź liczbę')

def check_combination(number):
    numbers = []
    if len(number) == 1:
        for i in list_of_numbers[(int(number))]:
            numbers.append(i)
        return numbers
    elif len(number) > 1:
        index = len(number)
        for i in range(index-1):
            d = len(list_of_numbers[int(number[i])])
            c = 0
            for j in range(d):
                j = 0
                while j<d:
                    indeks = list_of_numbers[int(number[i])][c] + list_of_numbers[int(number[i+1])][j]
                    j+=1
                    numbers.append(indeks)
                c+=1
        return numbers


#print(check_combination(number))

#task 3

import numpy as np
import pprint
text = "Hey there mate Matt, it’s nice to finally meet you!"
def format_text(text):


    text = text.split(' ')
    line = []
    line_width = 0
    lines = []
    words = text
    maxWidth = 16
    for word in words:
        if len(word) + line_width + len(line) > maxWidth:
            # Need to add justified line
            nspaces = len(line) - 1 if len(line) - 1 else 1
            for i in range(maxWidth - line_width):
                line[i % nspaces] += " "
            lines.append("".join(line))
            line = []
            line_width = 0
        line.append(word)
        line_width += len(word)

    last_line = " ".join(line)
    last_line = last_line.strip()
    last_line = last_line + " " * (maxWidth - len(last_line))
    lines.append(last_line)
    pp = pprint.PrettyPrinter(depth=2)

    for i in lines:
        pp.pprint(i)


print(format_text(text))