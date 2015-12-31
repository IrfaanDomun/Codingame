import sys
import math
import binascii
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
import binascii

def text_to_bits(text, encoding='utf-16', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(16 * ((len(bits) + 15) // 16))

def text_from_bits(bits, encoding='utf-16', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    
def caracter2binay(answer):
    current = answer[1]
    previous = answer[0]
    count = 1
    answer_final =""
    print >> sys.stderr, answer
    for i in answer[1:]:
        print >> sys.stderr,i
    for i in answer[1:] :
        #print >> sys.stderr,i,previous, i==previous,i is previous,int(i)==int(previous)
        if int(i) == int(previous):
            count +=1
        else : 
            
            if int(previous) ==0:
                answer_final = answer_final + "00 "
            else : 
                answer_final = answer_final + "0 "
    
            for j in range(count) :
                answer_final = answer_final +"0"
            answer_final = answer_final +" "
            count = 1 
        previous = i
        print >> sys.stderr, 'count',count,"answer",answer_final,"indic",i
    if int(i)==1:
        answer_final= answer_final +"0 "
    else :
        answer_final = answer_final +"00 "
        
    for k in range(count):
        answer_final = answer_final +"0"    
    return answer_final
####################################################        
nb_bit = 16
message = raw_input()
print >> sys.stderr,message,bin(int(binascii.hexlify(message), nb_bit))
answer =""
for i in message:
    answer = answer + bin(int(binascii.hexlify(i), nb_bit))[2:]
final_answer = ""
print >> sys.stderr, answer
answer1 = text_to_bits(message)[1:]
encoded = ""
tmp = ""
for ch in message:
    chBin = bin(ord(ch))[2:]
    while len(chBin) < 7:
        chBin = '0' + chBin
    tmp += chBin

#print >> sys.stderr,answer1, answer, answer==answer1, bin(ord(message)), tmp

final_answer = final_answer + caracter2binay(tmp)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr, final_answer
print final_answer
