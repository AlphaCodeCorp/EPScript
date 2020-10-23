import sys, getpass, getopt, requests, random, time, json
from math import *
from datetime import datetime
import os

print('Number of arguments : ', len(sys.argv))

print('#########################################')
print('')
print('Script download image from json Thomas')
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
    
    l = len(dataRequest)
    i=0
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for images in dataRequest:

        image = images['link-href']
        titre = image.split('/')

        response = requests.get(image)

        fold = folder + str(titre[-2])
        if os.path.exists(fold):
            print("Le fichier existe déjà")
        else:
            os.mkdir(fold)
        
        file_image = folder + str(titre[-2]) + "/" + str(titre[-1])
        
        file = open(file_image, "wb")
        file.write(response.content)
        file.close()

        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i=i+1



def getDataJson(link, folder):

        with open(link) as f:
            data = json.load(f)

        ## Download all image from json
        checkFolder(folder)
        download(data, folder)

        
        
def main(argv):
    link = 'D:\Projet Developpement\EPScript\csvjson.json'
    username = getpass.getuser()
    folder = ''
    username = getpass.getuser()

    try:
        opts, args = getopt.getopt(argv, "hs:f:", ["help", "subReddit=", "folder="])

    except getopt.GetoptError:
        print('You must call the script with this arguments \".\EP_Script_v2.py -s <sub> -f <folder>\"')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('You must call the script with this arguments \".\EP_Script_v2.py -s <sub> -f <folder> \"')
            print ('Example : .\\EP_Script_v2.py r\/EarthPorn D:/Users/username/Documents/ImageReddit/ 50')
            sys.exit()
        elif opt in ("-s", "--sub"):
            link = arg
        elif opt in ("-f", "--folder"):
            folder = arg
    
    if (link == ''):
        print('You must specified a file json !')
        sys.exit(2)
    elif (folder == ''):
        folder = 'C:/Users/' + username + '/Documents/Images_Scan/'
        print("You havn't specified a file. The default file is", folder)
    print("File: ", link, " folder: ", folder)
    
    getDataJson(link, folder)



##getDataJson('pp', 'mm', '06')
main(sys.argv[1:])
