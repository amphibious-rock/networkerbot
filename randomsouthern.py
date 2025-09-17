'''
Python Module for networkerbot to return a random southern EMU or DMU image link
Amphibious Rock
'''


from random import randint

def RandomSouthern():
    southern = [201,202,203,204,205,206,207,401,402,403,404,
            405,411,413,414,415,416,418,419,421,423,432]
    file_format = ["jpg","jpg","JPG","jpg","jpg","jpg","jpg","jpg","jpg","jpg","jpg",
            "jpg","jpg","jpg","jpg","JPG","jpg","jpg","jpg","JPG","jpg","jpg",]

    unit = randint(0,len(southern)-1)
    MainLink = "https://raw.githubusercontent.com/amphibious-rock/networkerbot/refs/heads/main/"
    FullLink = MainLink+str(southern[unit])+"."+str(file_format[unit])
    #print(FullLink)

    return [southern,unit,FullLink]
