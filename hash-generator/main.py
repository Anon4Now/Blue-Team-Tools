
import json
import os
import sys
import time
import hashlib
import datetime

from typing import KeysView
from pynput.keyboard import Key, Listener
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from vt_check import vtChecking

# Global vars used in script
hashList = []
currentState = []
patterns = ["*"]
ignore_patterns = None
ignore_directories = False
case_sensitive = True

# Will reset script upon init in case reset did not occur at end
def clean_script():
    if os.path.exists("list.txt"):

        os.remove("list.txt")
    
    else: pass
    
    currentState.clear()


# Checks SHA256 hash against Virus Total (VT) threat database and returns results if possible
def vtHashCheck():

    checkID = vtChecking.hashExists(hashList[0])
    checkIDJson = json.loads(checkID)

    if not 'error' in checkIDJson:
        lastStatsDict = {}

        extractLastAnalysisDate = datetime.datetime.fromtimestamp(checkIDJson['data']['attributes']['last_analysis_date'])
        extractLastAnalysisStats = checkIDJson['data']['attributes']['last_analysis_stats']
        
        print(f'Last Analysis Date : {extractLastAnalysisDate}')

        print(f'Last Analysis Stats:')
        for key in extractLastAnalysisStats:
            lastStatsDict[key] =  extractLastAnalysisStats[key]
            print(F'   {key}: {extractLastAnalysisStats[key]}')

        for key in lastStatsDict:
            if key == 'malicious':
                if lastStatsDict[key] == 0:
                    print(f'\nBased on results, the file appears safe')
                elif lastStatsDict[key] > 0 and lastStatsDict[key] < 2:
                    print(f'\nSome vendors flagged this file, consider additional research')
                elif lastStatsDict[key] > 2:
                    print(f'\nThis file may be malicious, consider not downloading')

    if 'error' in checkIDJson:
        extractErrorCode =  checkIDJson['error']['code']
        if extractErrorCode == 'NotFoundError':
            print(f'This file has not been uploaded to Virus Total before -- consider uploading the file for scanning at \n"https://www.virustotal.com/gui/home/upload"')

        elif extractErrorCode != 'NotFoundError':
            print(f'Error returned from VT is {extractErrorCode}')

        else:
            pass

# Methods that perform the "watchdog" capabilities on the path defined and the method that creates hashes
class eventMessage:

    # watch for "create" events in file path
    def on_created(event):
        if event:
            currentState.append(True)
    
    # watch for "modified" events in file path and write event to txt file in py path
    def on_modified(event):
      
        t = str(event.src_path)

        with open("list.txt", "w+") as file:
            file.write(t)

    # read from txt file created by on_modified and use data to generate hashes
    def callList():

        with open("list.txt") as file:
            data = file.read()
            print(f'[File Name] - {data}')            

            BLOCK_SIZE = 65536 # The size of each read from the file

            hash_sha256 = hashlib.sha256() # Create the hash object for SHA256 `.sha256()`
            hash_sha1 = hashlib.sha1() # Create the hash object for SHA1 `.sha1()`
            hash_md5 = hashlib.md5() # Create the hash object for MD5`.md5()'
            with open(data, 'rb') as f: # Open the file to read it's bytes
                fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
                while len(fb) > 0: # While there is still data being read from the file
                    hash_sha256.update(fb) # Update the hash
                    hash_sha1.update(fb) # Update the hash
                    hash_md5.update(fb) # Update the hash
                    fb = f.read(BLOCK_SIZE) # Read the next block from the file


            print(f'[SHA-256 Hash] - {hash_sha256.hexdigest()}') # Print the hash value to CLI
            print(f'[SHA-1 Hash] - {hash_sha1.hexdigest()}') # Print the hash value to CLI
            print(f'[MD5 Hash] - {hash_md5.hexdigest()}\n') # Print the hash value to CLI

            hashList.append(hash_sha256.hexdigest()) # Append the hash value to gloval list


# Event Handler Configurations
my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
my_event_handler.on_created = eventMessage.on_created
my_event_handler.on_modified = eventMessage.on_modified

# Define path and set "Observer" class from watchdog
path = 'C:/Users/tutko/Downloads/'
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

# Starts the observer, prints time left to download file, and invokes other func/methods if file is provided
def cliStart():
    my_observer.start()

    # show time left to download file on CLI
    print(f'Seconds Left to Download File...\n')
    for i in range(30,-1,-1):
            if not True in currentState:
                if i == 0:
                    sys.stdout.write(f'No File Given')
                    sys.stdout.flush()
                    time.sleep(1)
                else:
                    sys.stdout.write(str(i)+f' ')
                    sys.stdout.flush()
                    time.sleep(1)

            else:
                print(f'File seen - generating hashes...\n')
                sys.stdout.flush()
                break

    # call functions and sleep
    time.sleep(10)
    eventMessage.callList()
    time.sleep(3)
    vtHashCheck()
    time.sleep(1)
    clean_script()
    
            

if __name__ == "__main__":
    clean_script()
    print(f'Click <ENTER> to begin or <DELETE> to exit\n')
    
    # Keyboard event listener used to define when to start script
    def show(key):

        if key == Key.enter: # By pressing <ENTER> it starts the loop
            cliStart()

                
        if key == Key.delete: # By pressing <DELETE> button it terminates the loop 
            return False

    with Listener(on_press = show) as listener:
        listener.join()
    
    show()
    
