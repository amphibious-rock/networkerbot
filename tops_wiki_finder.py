import requests
import urllib.request
import httpx
from time import sleep
import os
import sys
from colorama import Fore, Back, Style

client = httpx.AsyncClient()
headers = {"User-Agent": "Networker Bot xxxxxxx@gmail.com"}
tops_class = 37
url=f"https://en.wikipedia.org/api/rest_v1/page/summary/British_Rail_Class_{tops_class}"
response = client.get(url,headers=headers)

def get_wiki_stuff(tops_class):
    
    url=f"https://en.wikipedia.org/api/rest_v1/page/summary/British_Rail_Class_{tops_class}"
    headers = {"User-Agent": "Networker Bot crowfoot960@gmail.com"}
    
    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        #page_title = data.get("title","No title found")
        #summary = data.get("extract","No summary available")
        thumbnail_url = data.get("thumbnail",{}).get("source","No image available")
        return thumbnail_url

f = open("valid_tops.txt","rt")
valid_tops = f.readline().split(",")
#print(valid_tops)
f.close()



f = open("tops_wiki_redirects.txt","rt")
redirects = []
for i in f:
    redirect = i.split(",")
    temp = redirect[1]
    redirect[1] = temp.strip("\n")
    redirects.append(redirect)
f.close()



need_exception = [] # tops that have an exception to speed up checking for redirects needed
for j in redirects:
    need_exception.append(j[0])




limit = 500 #what point to stop, testing only, leave at 1000 for entire list.
x=0
print(redirects)

delay = 0.25
passes = 1
if delay-(0.05*passes) < 0:
    passes = delay/0.05
for d in range(0,passes):
    x=0
    for train_original in valid_tops:
        sleep(delay)
        x+=1
        if x > limit:
            break
        
        
        train = train_original
        if train_original in need_exception:
            train = redirects[need_exception.index(train_original)][1]
        
        
        img=get_wiki_stuff(train)
        if img == "No image available":
            #need_exception.append(train)
            print(Fore.RED+train,"Image Fail"+Fore.RESET)
        else:
            file_size = 0
            n=0
            while file_size < 3000:
                n+=1
                if n == 4:
                    print(Fore.RED,train,"CRITICAL FAILURE",Fore.CYAN,"#X#X#X#X#",Fore.RESET)
                    break
                    
                thumb_url = img 
                data = requests.get(thumb_url, headers=headers).content
                
                # Opening a new file named img with extension .jpg
                # This file would store the data of the image file
                extension=".jpg"
                filename = train+extension
                f = open(filename,'wb')
        
                # Storing the image data inside the data variable to the file
                f.write(data)
                f.close()
                
                colour = Fore.GREEN
                if n > 1:
                    colour = Fore.YELLOW
                    sleep(0.25)
                    
                
            
                file_size = os.path.getsize(filename)
                print(colour,train,"File Size is :", file_size, "bytes"+Fore.RESET)
        print(Fore.GREEN+"Pass "+str(d+1)+"/"+str(passes),train,thumb_url,Fore.RESET)
        #print(img)
        #urllib.request.urlretrieve(img, "geeksforgeeks.png")#, headers=headers)
        
    delay -= 0.05


print(need_exception)
# 18 IMAGE FAIL
# 19 IMAGE FAIL
# 21_(NBL)
# 38 FAIL --> add to fail list for info
# 41_(Warship_Class)
# 43_(HST)
# 51 PROPOSED
# 62 PROPOSED
# 65 PROPOSED
# 75 PROPOSED
# 97 FAIL
# 129 IMAGE FAIL
# 301 IMAGE FAIL
# 316_(Picc-Vic)
# 382 FAIL
# 499 FAIL
# 780 FAIL
# 781 FAIL
# 820 FAIL
# 930 IMAGE FAIL
# 931 FAIL
# 932 FAIL
# 933 FAIL
# 937 FAIL
# 951 FAIL
# 960 IMAGE FAIL