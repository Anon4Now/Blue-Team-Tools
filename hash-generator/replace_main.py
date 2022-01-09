import os, sys, time

from watchingdog import Watchdog
from hash_generator import HashGenerator
from user_cli import GetUserOptions


fileName = "list.txt"


# Will reset script upon init in case reset did not occur at end
def clean_script():
    if os.path.exists(fileName):

        os.remove(fileName)

    else:
        pass


if __name__ == '__main__':
    clean_script()

    while True:
        userInput = input("\r[+] Would you like to start watching a folder [y/n]? >> ")

        getArgs = GetUserOptions()

        if userInput == 'y':
            path = getArgs.startWatchingPath()

            watcher = Watchdog(path)
            watcher.startObserver()

            print("[+] Seconds left to download file")
            checkForFile = getArgs.countDownToDownload()

            if not checkForFile:
                print("\r[-] No file detected, returning to start...")
                time.sleep(3)
                continue
            else:
                hashGen = HashGenerator(fileName)

                # call functions and sleep
                time.sleep(10)
                hashGen.startHash()
        #         # time.sleep(3)
        #         # vtHashCheck()
                time.sleep(1)
                clean_script()

        elif userInput == 'n':
            userInput = input("[+] Do you want to exit [y/n]? >> ")
            if userInput == 'y':
                print("[+] Closing program...")
                getArgs.stopWatching()
            elif userInput == 'n':
                continue
            else:
                print("[-] Unknown input, please enter 'y' or 'n'...")
                continue

        # fileDetected = False
        #
        # userInput = input("\r[+] Would you like to start watching a folder [y/n]? >> ")
        #
        # if userInput == 'y':
        #
        #     path = input("[+] Folder to be monitored, default is Downloads [enter file path or enter 'd' for default]? >> ")
        #
        #     if path == 'd':
        #         path = 'C:/Users/tutko/Downloads'
        #     else:
        #         pass
        #
        #     watcher = Watchdog(path)
        #
        #     # show time left to download file on CLI
        #     print(f'[+] Seconds Left to Download File...')
        #     for i in range(5, -1, -1):
        #         if not Watchdog.eventCheck:  # UPDATE THIS CLASS VAR FROM IMPORT
        #             if i == 0:
        #                 sys.stdout.flush()
        #                 sys.stdout.write(f'\r[-] No file detected, returning to start...')
        #
        #             else:
        #                 sys.stdout.write("\r" + str(i))
        #                 sys.stdout.flush()
        #                 time.sleep(1)
        #
        #         else:
        #             print(f'[+] File seen - generating hashes...\n')
        #             sys.stdout.flush()
        #             fileDetected = True
        #             break
        #
        #     if fileDetected:
        #
        #         # call functions and sleep
        #         time.sleep(10)
        #         # hashGen.startHash()
        #         # time.sleep(3)
        #         # vtHashCheck()
        #         time.sleep(1)
        #         clean_script()
        #     else:
        #         sys.stdout.flush()
        #         time.sleep(5)
        #         continue
        #
        # elif userInput == 'n':
        #     userInput = input("[+] Do you want to exit [y/n]? >> ")
        #     if userInput == 'y':
        #         print("[+] Closing program...")
        #         exit()
        #     elif userInput == 'n':
        #         continue
        #     else:
        #         print("[-] Unknown input, please enter 'y' or 'n'...")
        #         continue
        #
        # else:
        #     print("[-] Unknown input, please enter 'y' or 'n'...")
        #     continue
