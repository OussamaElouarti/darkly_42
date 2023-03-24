import requests

# get all the directories
def get_paths(ip):
    tab=[]
    fp = requests.get(ip).text
    fp = fp.split("\n")
    for i in fp:
        if len(i)>2 and i[0] == '<' and i[1] == 'a':
            tab+=[i[i.find('\"')+1:i.find('/')+1]]
    tab.pop()
    return tab


ip = "http://10.12.176.69/.hidden/"
tab1=get_paths(ip)
tab2=get_paths(ip+tab1[0])
tab3=get_paths(ip+tab1[0]+tab2[0])
print("starting...")
for i in tab1:
    for j in tab2:
        for k in tab3:
            mystr = requests.get(ip+i+j+k+'README').text
            for b in mystr:
                if b.isdigit():
                    print(mystr)
                    exit()
