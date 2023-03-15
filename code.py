import json
import os
import matplotlib.pyplot as plt

#FIRST PART: OBTAINING DATA OUT OF THE GENERATED loc.txt

#Variable declaration
list = []
aux = ''
n = 0
f = 0

fp = open(os.getcwd() + '/Documents/CIC/loc.txt')

#Counting number of lines
for i, line in enumerate(fp):
    f = f+1

f = int(f/13) #Number of 13 line paragraphs
 
fp.seek(0,0) #Resets the file pointer
                       
for count in range(f):
    line_numbers = [n, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10, n+11, n+12]
    aux = ''
    fp.seek(0,0)

    for i, line in enumerate(fp):

        if i in line_numbers:
            aux = aux + line
    
    json_aux = json.loads(aux)

    list.append(json_aux)
    
    n = n+13

print(list[15]['src'][2]['y'])
#print(list[2]['timeStamp'])

#SECOND PART: REPRESENTING THIS DATA IN 4 QUADRANTS

#Variable declaration
timestamp = []
E = []
Emax = 0
nPots = 8

#Timestamp array gets created
for i in range(len(list)):

    timestamp.append(list[i]['timeStamp'])

#Quadrant 1
for i in range(len(list)):

    for j in range(nPots):

        if list[i]['src'][j]['x'] > 0 and list[i]['src'][j]['y'] > 0:

            if list[i]['src'][j]['E'] > Emax:

                Emax = list[i]['src'][j]['E']

    E.append(Emax)
    Emax = 0

#Plotting graph
plt.plot(timestamp, E)
plt.title("Quadrant 1 (Driver)")
plt.xlabel("Timestamps")
plt.ylabel("E")
plt.show()

#Resetting E
E = []

#Quadrant 2
for i in range(len(list)):

    for j in range(nPots):

        if list[i]['src'][j]['x'] < 0 and list[i]['src'][j]['y'] > 0:

            if list[i]['src'][j]['E'] > Emax:

                Emax = list[i]['src'][j]['E']

    E.append(Emax)
    Emax = 0

#Plotting graph
plt.plot(timestamp, E)
plt.title("Quadrant 2")
plt.xlabel("Timestamps")
plt.ylabel("E")
plt.show()

#Resetting E
E = []

#Quadrant 3
for i in range(len(list)):

    for j in range(nPots):

        if list[i]['src'][j]['x'] < 0 and list[i]['src'][j]['y'] < 0:

            if list[i]['src'][j]['E'] > Emax:

                Emax = list[i]['src'][j]['E']

    E.append(Emax)
    Emax = 0

#Plotting graph
plt.plot(timestamp, E)
plt.title("Quadrant 3")
plt.xlabel("Timestamps")
plt.ylabel("E")
plt.show()

E = []

#Quadrant 4
for i in range(len(list)):

    for j in range(nPots):

        if list[i]['src'][j]['x'] > 0 and list[i]['src'][j]['y'] < 0:

            if list[i]['src'][j]['E'] > Emax:

                Emax = list[i]['src'][j]['E']

    E.append(Emax)
    Emax = 0

#Plotting graph
plt.plot(timestamp, E)
plt.title("Quadrant 4")
plt.xlabel("Timestamps")
plt.ylabel("E")
plt.show()