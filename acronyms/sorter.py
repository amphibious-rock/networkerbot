definitions = []
file = open("jargon.txt","rt")

for j in file:
    print(j)
    if len(j) > 1:
        definitions.append(j.split(","))
file.close()


parent = []
headers = definitions[0]
definitions.pop(0)
for i in definitions:
    child=[]
    for j in i:
        if "\n" in j:
            j_new=(j[:j.find("\n")]).strip(" ")
            print(j_new)
            child.append(j_new)
        else:
            child.append(j.strip(" "))
    parent.append(child)
definitions=parent
            

definitions.sort()
definitions.insert(0,headers)
print(definitions)

file=open("jargon.txt","wt")
for x in definitions:
    string = ""
    for y in x:
        string+= y+" , "
    string = string.strip(" , ")
    string+="\n"
    if len(string) > 4:
        print(string)
        file.write(string)
file.close()

