'''
 Automation script which accept file name. extract all URL's from that file and connect to that URL's

'''

from sys import *
import webbrowser 
import re
from urllib.request import urlopen 

def  is_connected():
	try:
		urlopen('http://www.kite.com',timeout=5)
		return True

	except Exception as err:
		return False	

def Find(string):
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*/(/), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
	return url

def webLauncher(path):
	with open(path) as fp:
		for line in fp:
			print(line)
			url = Find(line)
			print(url)
			for str in url:
				webbrowser.open(str,new = 2)	

def main():

    print("------------------- Automation 1 ---------------------")
    print("Script Name : ",argv[0])

    if((len(argv) != 2)):
        print("Invalid Number of Arguments.....")
        print("Use -u flag for ussage...")
        print("Use -h flag for Help.....")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : Script is used to traverse the Specific Directory and delete duplicate files...")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : ApplicationName AbsolutePath_of_Directory Extension")
        exit()

        
    try:

    	connected = is_connected()
       
    	if connected:
       		webLauncher(argv[1])
    	else:
       		print("Unable to connect to internet....")

    except ValueError:
        print("Error : Invalid datatype of input...")    

    except Exception as E:
        print("Error : Invalid input",E)
        

    print("Application gets Terminated.....")            


# Starter of the automation script
if __name__ == '__main__':
        main()  