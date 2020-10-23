import sys, getpass, getopt, requests, random, time
from math import *
from datetime import datetime
import os

print('Number of arguments : ', len(sys.argv))

print('#########################################')
print('')
print('Script récupération d\'images sur Reddit')
print('')
print('#########################################')

## need link subreddit
## --link -l
## need nb d'image à récupérer
## --number -n
## folder destination
## --folder -f
##help
## --help -h

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def checkFolder(folder):

    if os.path.exists(folder):
        print("Le fichier existe déjà")
    else:
        os.mkdir(folder)

def download(dataRequest, folder):
    
    l = len(dataRequest['data']['children'])
    i=0
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for images in dataRequest['data']['children']:

        image = images['data']['url']
        titre = image.split('/')

        response = requests.get(image)

        file_image = folder + str(titre[-1])

        while os.path.exists(file_image):
            now = datetime.now()
            random.seed(str(now.strftime("%S")))
            file_image = folder + str(random.randint(0,99)) + str(titre[-1])
            break

        file = open(file_image, "wb")
        file.write(response.content)
        file.close()

        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i=i+1



def getDataJson(link, folder, number):

    print("Download images from https://www.reddit.com/r/" + link )

    limit = 100
    after = ''

    iteration = ceil(int(number)/limit)
    rest = int(number)%limit
    print(iteration)
    print(rest)

    for i in range(0, iteration):

        if i == 0 and int(number) > 100:
            print("First request with max limit")
            url = 'https://www.reddit.com/r/' + link + '.json?limit=' + str(limit)
        elif i == 0 and int(number) <= 100:
            print("First request with " + str(number) + " in limit")
            url = 'https://www.reddit.com/r/' + link + '.json?limit=' + str(number)
        elif i == iteration-1:
            print("request with limit parameter and after parameter" + after + " " + str(rest))
            url = 'https://www.reddit.com/r/' + link + '.json?limit=' + str(rest) + "&after=" + after
        else:
            print("request with after in parameter and max limit " + after + " " + str(limit))
            url = 'https://www.reddit.com/r/' + link + '.json?limit=' + str(limit) + "&after=" + after
        
        ## Make the request
        r = requests.get(url, headers = {'User-agent': 'Zbi 1'})
        
        ##parse request in json format
        data = r.json()
        
        ## Download all image from json
        checkFolder(folder)
        download(data, folder)

        after = data['data']['after']
        print("After: " + after)
        
        
def main(argv):
    link = ''
    username = getpass.getuser()
    folder = ''
    number = '25'
    username = getpass.getuser()

    try:
        opts, args = getopt.getopt(argv, "hs:f:n:", ["help", "subReddit=", "folder=", "number="])

    except getopt.GetoptError:
        print('You must call the script with this arguments \".\EP_Script_v2.py -s <sub> -f <folder> -n <number>\"')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('You must call the script with this arguments \".\EP_Script_v2.py -s <sub> -f <folder> -n <number>\"')
            print ('Example : .\\EP_Script_v2.py -s EarthPorn -f D:\\Users\\username\\Documents\\ImageReddit\\ -n 50')
            sys.exit()
        elif opt in ("-s", "--sub"):
            link = arg
        elif opt in ("-f", "--folder"):
            folder = arg
        elif opt in ("-n", "--number"):
            number = arg
    
    if (link == ''):
        print('You must specified a subreddit !')
        sys.exit(2)
    elif (folder == ''):
        folder = 'C:\\Users\\' + username + '\\Documents\\Images_SubReddit_test\\'
        print("You havn't specified a file. The default file is", folder)
    print("Sub: ", link, " folder: ", folder, " number: ", number)
    
    getDataJson(link, folder, number)



##getDataJson('pp', 'mm', '06')
main(sys.argv[1:])
