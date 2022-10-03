import urllib.request

# get all the directories
def get_paths(ip):
    tab=[]
    fp = urllib.request.urlopen(ip)
    mystr = fp.read().decode("utf8")
    fp.close()
    mystr = mystr.split('\n')
    for i in mystr:
        if len(i)>2 and i[0] == '<' and i[1] == 'a':
            tab+=[i[i.find('\"')+1:i.find('/')+1]]
    tab.pop()
    return tab


ip = input('Enter the ip address to the .hidden folder: ')
tab1=get_paths(ip)
tab2=get_paths(ip+tab1[0])
tab3=get_paths(ip+tab1[0]+tab2[0])

for i in tab1:
    for j in tab2:
        for k in tab3:
            fp = urllib.request.urlopen(ip+i+j+k+'README')
            mystr = fp.read().decode("utf8")
            fp.close()
            for b in mystr:
                if b.isdigit():
                    print(mystr)
                    exit()
