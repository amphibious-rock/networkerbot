#print("Initialisating")

def fetch_tops():
    print("1/2 Fetching valid TOPS.",end=" ")
    f = open("valid_tops.txt","rt")
    data = f.readline()
    valid_tops = data.split(",")
    print("Fetched.",end=" ")
    f.close()
    
    print("2/2 Fetching valid TOPS.",end=" ")
    f = open("tops_wiki_redirects.txt","rt")
    redirects = []
    for redirect in f:
        redirects.append(redirect.split(","))
    f.close()
    print("Fetched.")
    
    return valid_tops, redirects 

def fetch_token():
    f = open("token.txt","rt")
    token = f.readline()
    f.close()
    print("fetched bot token")
    return token
    