import sys
import operator
import functools 

w = dict({})

q= sys.argv[1]

p = open(q,'r') #open file r.txt

lines = p.readlines() #read file

#with open(q, 'r') as f:

for line in lines:

    for string in line.split():

        if string.lower() in w.keys():

            w[string.lower()] += 1
        else:

            w[string.lower()] = 1

List = sorted(w.items(), key = operator.itemgetter(1), reverse = True) #Sort alg

#Print words that end in "in"

print ("Words end in "in": ")

print(" ")

for z in List:

    if len(z[0]) > 1  and z[0][-2] == 'i' and z[0][-1] == 'n' and len(z[0]) > 4:
  
       if z[1] > 1:

             print(z[0], "occurs", z[1], "times")
       else:

             print(z[0], "occurs", z[1], "time")

print(" ")

#Counts how many different words are listed 

print ("Counting each different word: ") 

for a in List:

     if len(a[0]) > 1  and a[0][-2] != 'i' and a[0][-1] != 'n' and len(a[0]) > 4:

        #Turn tuples into string

        aTuple = a[0];

        aList = list(aTuple)             

        res = (((''.join([''.join(sub) for sub in aList])))) 

        res1 = len((((''.join([''.join(sub) for sub in aList]).split()))))#count number of strings in a list
        
       # resCount = len(aList) print total number of characters in a string? Basically confirms the strings are in a list of their own for my code.

        if a[1] > 1:

           print(res, "counts as", a[1])

           #print("Total number of words in string - ", res1)

        else:

           print(res, "counts as", a[1])

           #print("Total number of words in string - ", res1)

           #for item in res:
            #   print len(item.split())
        
#Total number of words in the file

print(" ")

file = open(q, "r") #find the file r.txt

data = file.read() #read

words = data.split() #splits string into list

#count = len(line.split()) 

#print ("Total number of words in the string are : " +  str(count)) 

print('Number of words in text file :', len(words)) #counts all words including duplicates 
