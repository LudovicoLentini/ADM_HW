#Write a function
def is_leap(year):
    leap = False
    
    if year%4==0 :
        if year%100==0 : 
            if year%400 ==0 :
                leap= True
        else:
            leap= True
    
    
    return leap

#Print function
n=int(input())
for i in range(n):
    print(i+1,end="")
#Say "Hello, World!" With Python
if __name__ == '__main__':
    print ("Hello, World!")

#Python If-Else

n = int(input().strip())
if n % 2 == 0:
    if n in range(2,6):
        print("Not Weird")

    elif n in range(6,21):
        print("Weird")

    elif n > 20:
        print("Not Weird")
else:
    print("Weird")

#Arithmetic Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

#Python:Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
#Loops
if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print(i**2)

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result= [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)]
print(result)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
Max=max(A)
A.sort(reverse=True)
Runner_Up=0
i=0
while i < n:
    i_simo= A[i]
    if(Max>i_simo):
        Runner_Up = i_simo
        i=n
    i+=1

print(Runner_Up)

#Nested Lists
if __name__ == '__main__':
    my_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name,score])
        
sorted_set_scores= sorted(list(set([X for name, X in my_list])))
second_highest = sorted_set_scores[1]
Result_list=[]
#for name, score in my_list:
#    if score == second_highest:
#        Result_list.append(name)

[Result_list.append(name) for name,score in my_list if score==second_highest]
Result_list.sort()        
[print(x) for x in Result_list ]

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
score = student_marks[query_name]
result= float(sum(score)/len(score))
print('%.2f'%(result))

#Lists
if __name__ == '__main__':
    N = int(input())
    Command_list=[]
    for i in range(N):
        line=input()
        Command_list.append(line)
#print(My_list)
My_list=[]
for i in range(N):
    #print(My_list[i])
    One_Line= Command_list[i].split()
    First_El=One_Line[0]
    if First_El=="insert":
        My_list.insert(int(One_Line[1]),int(One_Line[2]))
    elif First_El== "print":
        print(My_list)
    elif First_El == "remove":
        #print(int(One_Line[1]))
        My_list.remove(int(One_Line[1]))
    elif First_El== "append":
        My_list.append(int(One_Line[1]))
    elif First_El== "pop":
        My_list.pop()
    elif First_El== "sort":
        My_list.sort()
    elif First_El== "reverse":
        My_list.reverse()

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    #integer_list=list(integer_list)
    Tuple_list=tuple(integer_list)
    print(hash(Tuple_list))
    
#sWAP cASE
def swap_case(s):
    return s.swapcase()

#String Split and Join
def split_and_join(line):
    Splitted_list=line.split()
    result = "-".join(Splitted_list)
    return result

#Whats your name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    return(print('Hello ',first," ",last,"! You just delved into python.",sep=""))


#Mutuations
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    new_string = ''.join(l)    
    return new_string

#Find a string
def count_substring(string, sub_string):
    n=len(string)
    Len_sub=len(sub_string)
    count=0
    for i in range(n-Len_sub+1):
        if string[i:i+Len_sub]== sub_string:
            count+=1
    return count

#String Validators
if __name__ == '__main__':
    s = input()

#for oper in ("isalnum", "isalpha","isdigit","islower","isupper"):
#    #List=[]
 #   any(eval("el." + oper + "()") for el in s)
  #  #print(any(List))

print(any(ch.isalnum() for ch in s))
print(any(ch.isalpha() for ch in s))
print(any(ch.isdigit() for ch in s))
print(any(ch.islower() for ch in s))
print(any(ch.isupper() for ch in s))

#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#text wrap

def wrap(string, max_width):
    N= len(string)
    New_string=""
    count=0
    for i in range(N):
        New_string += string[i]
        count+=1
        if count == max_width:
            count=0
            New_string+= "\n"
        
    return New_string

#Designer Door mat

Data = input()
Data=Data.split()
N=int(Data[0])
M=int(Data[1])

#Declaring the Half way number, to stop and print Welcome
N_half= int(N/2 - 0.5)
#Declaring the pattern decoration
Deco=".|." 

#UPPER PATTERN: scaling the patter according to index n_times
n_times=1
for i in range(N_half):
    Decoration=Deco*n_times
    print(Decoration.center(M,"-"))
    n_times=n_times+2

#MID PATTERN: WELCOME 
print("WELCOME".center(M,"-"))

#LOWER PATTERN: scaling the Deco according to n_times, starting from before
n_times=n_times-2 #taking away the 2 of the last cicle
for i in range(N_half):
    Decoration=Deco*n_times
    print(Decoration.center(M,"-"))
    n_times=n_times-2

    

#String Formatting
def print_formatted(number):
    
    #width of the max number to represent, to be utilized in the rjust
    
    #Cutting two first elem because not part of the number itself but formatting element
    width = len(bin(number)[2:])
    
    for i in range(number):
        print(str(i+1).rjust(width," "), end=" ")
        print(oct(i+1)[2:].rjust(width, " "), end=" ")
        print((hex(i+1)[2:].upper()).rjust(width," "),end=" ")
        print(bin(i+1)[2:].rjust(width," "),end=" ")
        print("")
#Using rjust to make the same width of columns for all the formatting columns


#Alphabet Rangoli
def print_rangoli(size):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    width=size*4-3
    #Index going from size to negative size,the abs() giv
    for i in range(size-1,-size,-1):
        letters=alphabet[abs(i):size] #cutting the alp to desired set of letters
        rev=letters[::-1] #reversing the letters
        Finaltext=rev + letters[1:] #taking the reversed+normal letters
        single_row= "-".join(Finaltext) #spacing with "-"
        print(single_row.center(width,"-")) #centering with "."
        

#Capitalize!

# Complete the solve function below.
def solve(s):
    Result=""
    List_name=s.split(" ")
    for el in List_name:
        if el.isalpha():
            if el[0].isupper():
                Result=Result + el + " "
            else:
                modified=el[0].upper()+el[1:]
                Result=Result + modified +" "
        else:
            Result=Result + el + " "            
    return Result


#introductions to Sets
def average(array):
    set_of_a= set(array)
    return (sum(set_of_a)/len(set_of_a))


#The Minion Game
def is_vowel(letter):
    result = 0
    if letter in "AEIOU":
        result=1
    return result



def minion_game(string):
    St_Points=0
    Kev_Points=0
    

    for i in range(len(string)):
        if string[i] in "AEIOU":
            Kev_Points=Kev_Points + len(string)-i
        else:
            St_Points=St_Points+ len(string)-i
        
        
        
    
    if St_Points>Kev_Points:
        print ("Stuart" + " " + str(St_Points))
    elif St_Points< Kev_Points:
        print ("Kevin" + " " + str(Kev_Points))
    else:
        print("Draw")



#Merge the Tools!
def merge_the_tools(string, k):
    temporary=[]
    index=0
    for el in string:
        index+=1
        if el not in temporary:
            temporary.append(el)
        if index==k:
            print ("".join(temporary))
            temporary=[]
            index=0
        
        
#No Idea!
n, m = input().split()
Array = input().split()
A = set(input().split())
B = set(input().split())

points=0
for el in Array:
    if el in A:
        points+=1
    elif el in B:
        points-=1

print (points)


#Symmetric Difference!
# Enter your code here. Read input from STDIN. Print output to STDOUT
M= int(input())
a=set(map(int,input().split()))
N= int(input())
b=set(map(int,input().split()))


c=a.difference(b).union(b.difference(a))
c=list(c)
c.sort()
for el in c:
    print(el)
#print(M,a,N,b)


#Set.add()

N= int(input())
s=set()
for i in range(N):
    s.add(input())
    
print(len(s))

#Set.discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    Lista_riga= input().split()
    if Lista_riga[0]=="pop":
        s.pop()
    elif Lista_riga[0]=="remove":
        s.remove(int(Lista_riga[1]))
    elif Lista_riga[0]=="discard":
        s.discard(int(Lista_riga[1]))

Result= sum(s)
print(Result)

#Set .union() Operation
n = int(input())
Eng = set(map(int, input().split()))
b=int(input())
Fr = set(map(int, input().split()))

Tot=Eng.union(Fr)

print(len(Tot))


#Set .intersection() Operation
n= int(input())
Eng = set(map(int, input().split()))
b=int(input())
Fr = set(map(int, input().split()))

Tot=Eng.intersection(Fr)

print(len(Tot))

#Set .difference() Operation
n = int(input())
Eng = set(map(int, input().split()))
b=int(input())
Fr = set(map(int, input().split()))

Tot=Eng.difference(Fr)

print(len(Tot))


#Set .symmetric_difference() Operation
n = int(input())
Eng = set(map(int, input().split()))
b=int(input())
Fr = set(map(int, input().split()))

Tot=Eng.symmetric_difference(Fr)

print(len(Tot))

#Set Mutations

N_a = int(input())
A = set(map(int, input().split()))
N=int(input())
for i in range(N):
    Command,num= input().split()
    B = set(map(int, input().split()))
    
    if Command=="intersection_update":
        A.intersection_update(B)
    elif Command=="update":
        A.update(B)
    elif Command=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif Command== "difference_update":
        A.difference_update(B)
print(sum(A))


#The Captain's Room
K=int(input())
List_N= list(map(int, input().split()))
#Idea 3
Set1=set()
Set2=set()
for el in List_N:
    if el not in Set1:
        Set1.add(el)
    else:
        Set2.add(el)
Final_Set=Set1.difference(Set2)

[print(el) for el in Final_Set]


#Check subset
T=int(input())
for i in range(T):
    N_A=int(input())
    A = set(map(int, input().split()))
    N_B=int(input())
    B = set(map(int, input().split()))
    
    if A.issubset(B):
        print("True")
    else:
        print("False")
        
#Check Strict Superset
A = set(map(int, input().split()))
N=int(input())
List=[]
for i in range(N):
    B = set(map(int, input().split()))
    List.append(A.issuperset(B))
print(all(List))

#collections.Counter()
from collections import Counter

X= int(input())
Shoe_List= list(map(int, input().split()))
Shoe_count=Counter(Shoe_List)

Money=0
N=int(input())
for i in range(N):
    shoe_size, x_i= map(int,input().split())
    if shoe_size in Shoe_count.keys():
        Money+= x_i
        Shoe_List.remove(shoe_size)
        Shoe_count=Counter(Shoe_List)

print(Money)

#DefaultDict Tutorial
  
from collections import defaultdict
n,m = list(map(int, input().split()))
d = defaultdict(list)

lista_elem=[]
for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    lista_elem=lista_elem + [input()]  

#print(d)
#print(lista_elem)
'''
for i in lista_elem: 
    if i in d:
        print (" ".join( map(str,d[i]) ))
    else:
        print -1
'''
        
for i in lista_elem:
    if len(d[i]) > 0:
        print(" ".join(str(c) for c in d[i]))
    else:
        print(-1)


#Collections.namedtuple()
N=int(input())
from collections import namedtuple
Student = namedtuple("Student",input().split())

Tot=0
for i in range(N):
    First,Second,Third,Four=input().split()  
    Stud= Student(First,Second,Third,Four)
    Tot += int(Stud.MARKS)

print("{:.2f}".format(Tot/N))
    
    
#Collections.OrderedDict()
N=int(input())
from collections import OrderedDict
FinalList= OrderedDict()
for i in range(N):
    rows=input().split()
    if(len(rows)==2):
        item_name=rows[0]
        key_price=rows[1]
    if (len(rows)==3):
        item_name=rows[0] + " " + rows[1]
        key_price=rows[2]
    ##now in item_name and key_price
    if item_name not in FinalList:
        FinalList[item_name] = int(key_price)
    else:
        FinalList[item_name] += int(key_price)

#print(FinalList)
for el in FinalList:
    print(el, FinalList[el])


#Word Order
N=int(input())
from collections import OrderedDict
Words=OrderedDict()
for i in range(N):
    row=input()
    if row in Words:
        Words[row] +=1
    else:
        Words[row]=1

print(len(Words))
for el in Words:
    print(Words[el],"", end="")    

#Collections.deque()
N=int(input())
from collections import deque
d = deque()
for i in range(N):
    row=input().split()
    if row[0] == "append":
        d.append(row[1])
    elif row[0] == "appendleft":
        d.appendleft(row[1])
    elif row[0]=="pop":
        d.pop()
    elif row[0]=="popleft":
        d.popleft()
[print(el, end=" ") for el in d ]

#Piling Up!
T= int(input())
from collections import deque
for _ in range(T):
    N=int(input()) 
    d=deque(map(int, input().split()))
    
    Control= "Yes"
    maxim=max(d[0],d[-1])
    while d:   
        if d[0]>=d[-1]:
            elem = d.popleft()
        else:
            elem=d.pop()
        if maxim>=elem:
            maxim=elem
        else:
            Control="No"
            break 
    
    print(Control)
        
 #  Company Logo 

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    c=Counter(sorted(s))
    
    soluz=c.most_common(3)
    for el in soluz:
        print(*el)
    
#Detect Floating Point Number
T=int(input())
import re
for i in range(T):
    s=input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s)))

#Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

#Group(), Groups() & Groupdict()
import re
s=input()
m = re.search(r"([a-z0-9])\1+", s)
print(m.group(1) if m else -1)


#Re.findall() & Re.finditer()
import re

s = '[qwrtypsdfghjklzxcvbnm]'
pattern='(?<=' + s +')([aeiou]{2,})' + s

a=re.findall(pattern,input(),re.I)
if a==[]:
    print(-1)
else:
    for i in a:
        print(i)


#Re.start() & Re.end()
import re
s = input()
k = input()

index = 0
if re.search(k, s):
    while (index+len(k) < len(s)):
        #print("index : ", index)
        m = re.search(k, s[index:]) #begins search with new index
        #print(m)
        if not m:
        #    print("BREAK")
            break
            
        print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        #print("m.start:", m.start())
        index += m.start() + 1 
    
else:
    print((-1, -1))

#Regex Substitution
N=int(input())
import re

for _ in range(N):
    line=input()
    print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', (lambda m: 'and' if m.group(1) == '&&' else 'or'), line))
 
    
#Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

