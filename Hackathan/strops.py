li = []
def getspan(s, sub):
    span = []
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            #print("substring not found")
            break
        end = start + len(sub)
        span.append((start, end))
        start += 1
    print(len(span), span)
s = input("Enter a string to be matched with: ")
sub = input("Enter a substring to be matched: ")
getspan(s, sub)
#2.Reverseword(S)
def reverseword(s):
     return (s[::-1])
# word=input("Print a reverseword:")
# word_string = reverseword(word)
# print(word_string)



#3.removepunctuation(s)
import string
def removepunctuation(s):
     for i in s:
       if i not in string.punctuation:
            print(i,end="")
# value=input("Enter a punctuation sentence:")
# removepunctuation(value)

#4.countWords(s)
def countWords(s):
    words = s.split()
    return len(words)

word=input("Print a coundWord:")
word_string= countWords(word)
print(word_string)

#5.charecterMap(s)
from collections import Counter
def characterMap(s):
   return dict(Counter(s))

value= input("Enter charactermap sentence:")
result=characterMap(value)
print(f"mapped characters: {result}")

#6.MakeTitle(s)
def maketitle(s):
    return s.title()  

word = input ("Enter a string to make a title: ")  
word_string = maketitle(word)
print(word_string)

#7.Normalizespaces
def normalizeSpaces(s):
    return ' '.join(s.split())
space =input ("print a word:")
space_string = normalizeSpaces(space)
print(space_string)

#8.Transform
def transform(s):
    reverse=s[::-1]
    swapping=reverse.swapcase()
    print(swapping)
value=input("Enter a transform words:")
transform(value)

#9.getpermutation(s)
import itertools 
def getPermutation(s):
    permutations = itertools.permutations(s)
    return sorted(''.join(p) for p in permutations)
value=input("Enter a permutation words:")
result = getPermutation(value)
print(result)