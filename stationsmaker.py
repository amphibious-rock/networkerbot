'''
Code to generate the array style of list of stations.
converts bare txt file to array style.
DO NOT RUN THIS FILE.
converted array is in randomstation.py

AmphibiousRock
'''


f = open("stations.txt","rt")
from time import sleep
stations = []

print("1/3 | Importing Stations")
sleep(2)



for i in f:
    #line = f.readline()
    line = i
    stations.append(line)
    sleep(0.02)
    #print(line)
    length = len(stations)
    print(f"\rImporting... {length} Stations", end="")
f.close()

print("1/3 |",len(stations),"Stations Imported.")
sleep(5)
count = 0
for g in stations:
    #print(g)
    count+=1
    print(f"\rRecalling... {count} Stations", end="")
    
print("2/3 | Stations Recalled")
sleep(2.5)
print("3/3 | Exporting Stations...")
sleep(2.5)

s = open("station2.txt","at")
x=0
y=0
length = len(stations)
for i in stations:
    x+=1
    y+=1
    linev2 = "["+i+"],"
    s.write(linev2)
    #print(linev2)
    print(f"\rExporting... {y} / {length}Stations", end="")
    sleep(0.01)
    if x==100:
        s.close()
        print("saving...")
        s = open("Station2.txt","at")
        x=0
    
s.close()

print("3/3 |",len(stations),"Stations Exported To \" station2.txt \"")
sleep(0.5)

print("Complete.")
