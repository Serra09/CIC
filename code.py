import json
import os

#Variable declaration
list = []
aux = ''
n = 0
f = 0

fp = open(os.getcwd() + '/Documents/CIC/prueba.txt')

for i, line in enumerate(fp):
    f = f+1

f = int(f/13) #Number of 13 line paragraphs
fp = open(os.getcwd() + '/Documents/CIC/prueba.txt') #Resets the file pointer

for count in range(f):
    line_numbers = [n, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10, n+11, n+12]
    for i, line in enumerate(fp):

        if i in line_numbers:
            aux = aux + line

    fp2 = open(os.getcwd() + '/Documents/CIC/aux.json', 'w+')

    fp2.write(aux)

    json_aux = json.loads(aux)

    list.append(json_aux)

    n = n+13

print(list)
print(list[1]['src'][1]['x']) #:)
#print(list[0]['src']) #:)