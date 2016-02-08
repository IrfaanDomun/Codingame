import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
"""""
Create a dictionnary containing the value of each letter
"""
temp =""
a = "e, a, i, o, n, r, t, l, s, u"
a = a.split(",")
temp = temp + ",".join( [ "\""+i.replace(" ","")+"\""+":1" for i in a])
a = "d, g"
a = a.split(",")
temp = temp +"," + ",".join( [ "\""+i.replace(" ","")+"\""+":2" for i in a])
a = "b, c, m, p"
a = a.split(",")
temp = temp +"," + ",".join( ["\""+i.replace(" ","")+"\""+":3" for i in a])
a = "f, h, v, w, y"
a = a.split(",")
temp = temp +"," + ",".join( [ "\""+i.replace(" ","")+"\""+":4" for i in a])
a = "k"
a = a.split(",")
temp = temp+","  + ",".join( [ "\""+i.replace(" ","")+"\""+":5" for i in a])
a = "j,x"
a = a.split(",")
temp = temp +"," + ",".join( [ "\""+i.replace(" ","")+"\""+":8" for i in a])
a = "q,z"
a = a.split(",")
temp = temp +"," + ",".join( [ "\""+i.replace(" ","")+"\""+":10" for i in a])
dic = eval( "{"+ temp + '}')

"""""
Function to count point of a word
"""
def count_point(word):
    temp_count = 0
    for i in word:
        temp_count += dic[i]
    return temp_count
"""""
Check if you can make the word with the letters
"""
def check_word(word):
    letters_temp = letters[:]
    #print >> sys.stderr, word,letters
    if len(word) > len(letters):
        return False
    
    for i in letters_temp:
        if i in word:
            word = word.replace(i,"",1)            
    if word == "":
        return True
    else :
        return False    
"""""
Guetting the data
"""
list_word = {}
n = int(raw_input())
for i in xrange(n):
    w =  raw_input()
    list_word[w] = count_point(w)
letters = raw_input()
"""""
Sort the word by the most rewarding word
"""
sorted_list = sorted(list_word, key = lambda k : list_word[k], reverse = True)
""""
Print the first more rewarding word we can make
"""
for i in sorted_list:
    if check_word(i):
        print i
        break

