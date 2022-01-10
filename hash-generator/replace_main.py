import os, time, json

from watchingdog import Watchdog
from hash_generator import HashGenerator
from user_cli import GetUserOptions
from vt_check import VTChecking


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
        userInput = input("\r[+] Would you like to start watching a folder? [y/n] >> ")

        getArgs = GetUserOptions()

        if userInput == 'y':
            path = getArgs.startWatchingPath()

            watcher = Watchdog(path)
            isStarted = watcher.startObserver()

            if isStarted:
                print("[+] Seconds left to download file")
                checkForFile = getArgs.countDownToDownload()

                if not checkForFile:
                    print("\r[-] No file detected, returning to start...")
                    time.sleep(3)
                    continue
                else:
                    hashGen = HashGenerator(fileName)

                    # generate hashes
                    time.sleep(10)
                    sha256HASH = hashGen.startHash()
                    time.sleep(5)

                    # check to see if user wants to use API
                    while True:
                        useAPI = getArgs.useVirusTotal()
                        if useAPI:
                            vt = VTChecking()
                            response = vt.hashExists(sha256HASH)
                            checkIDJson = json.loads(response)

                            if 'error' not in checkIDJson:
                                vt.parseJson(checkIDJson)
                                break

                            if 'error' in checkIDJson:
                                vt.checkError(checkIDJson)
                                break

                        elif not useAPI:
                            checkInput = input("[+] Would you like to exit to start? [y/n] >> ")
                            if checkInput == 'y':
                                break
                            elif checkInput == 'n':
                                continue
                        else:
                            print("[-] Unknown entry, please use 'y' or 'n'...")
                            continue
                    time.sleep(1)
                    clean_script()
            else:
                print("[-] File path unknown, returning to start...")

        elif userInput == 'n':
            userInput = input("[+] Do you want to exit? [y/n] >> ")
            if userInput == 'y':
                print("[+] Closing program...")
                getArgs.stopWatching()
            elif userInput == 'n':
                continue
            else:
                print("[-] Unknown input, please enter 'y' or 'n'...")
                continue
