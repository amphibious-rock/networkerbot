from colorama import Fore


'''
Dylan Anticrack 5000
copyright (c) 2026 amphibious_rock
GNU General Public License 3.0
'''

def anticrack(txt):
    txt = txt.lower() #converts to lowercase
    alphabet = "qwertyuiopasdfghjklzcvnbm" #alphabet but without x
    crack = [["c","k","q"], #alternative characters array
             ["r"],
             ["a","@","4","0"],
             ["h"]]
    
    crack_b = [["c","k","q"], # alternative characters array for separate algorithm
             ["r"],
             ["a"],
             ["h"]]
    
    progress = [[False,crack[0]], [False, crack[1]], [False,crack[2]], [False,crack[0]], [False, crack[0]] ]
    progress_b = [[False,crack_b[0]], [False, crack_b[1]], [False,crack_b[2]], [False,crack_b[0]], [False, crack_b[0]] ]
    special_chars = 0
    alphabet_chars = 0
    
    progress_n = 0
    progress_b_n = 0
    for i in txt:
        
        if i in progress_b[progress_b_n][1]:
            progress_b[progress_b_n][0] = True
            
            progress_b_n +=1
            alphabet_chars+=1
        
        elif (not (i in alphabet)) or (i == "x"):
            if progress_b_n > 0:
                progress_b[progress_b_n][0] = True
                progress_b_n +=1
                special_chars+=1
            
        
        if i in progress[progress_n][1]:
            progress[progress_n][0] = True
            
            progress_n +=1
        
        if progress_n >= 5 and progress_b_n >= 5:
            break
        
        
    progress_count = 0
    for char in progress:
        if char[0] == True:
            progress_count+=1
            
    progress_count_b = 0
    for char in progress_b:
        if char[0] == True:
            progress_count_b+=1
    
    if progress_count >= 4 or (progress_count_b >= 3 and alphabet_chars >= 3):
        return True
    else:
        return False
