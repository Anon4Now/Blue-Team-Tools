import os, sys, time

from watchingdog import Watchdog
from user_cli import GetUserOptions
from hash_generator import HashGenerator


# Will reset script upon init in case reset did not occur at end
def clean_script():
    if os.path.exists("list.txt"):

        os.remove("list.txt")

    else:
        pass


if __name__ == '__main__':
    clean_script()

    while True:

        userInput = input("Would you like to start watching a folder? y/n")

        userOpts = GetUserOptions()
        outArgs = userOpts.checkOptions()

        watcher = Watchdog(outArgs['folder'])

        hashGen = HashGenerator("list.txt")

        if userInput == 'y':

            # show time left to download file on CLI
            print(f'Seconds Left to Download File...\n')
            for i in range(30, -1, -1):
                if not Watchdog.eventCheck:  # UPDATE THIS CLASS VAR FROM IMPORT
                    if i == 0:
                        sys.stdout.write(f'No File Given')
                        sys.stdout.flush()
                        time.sleep(1)
                    else:
                        sys.stdout.write(str(i) + f' \r')
                        sys.stdout.flush()
                        time.sleep(1)

                else:
                    print(f'File seen - generating hashes...\r\n')
                    sys.stdout.flush()
                    break
            # call functions and sleep
            time.sleep(10)
            hashGen.startHash()
            # time.sleep(3)
            # vtHashCheck()
            time.sleep(1)
            clean_script()

        elif userInput == 'f':
            userInput = input("Do you want to exit? y/n")
            if userInput == 'y':
                exit()
            elif userInput == 'n':
                continue
            else:
                print("Unknown input, please enter 'y' or 'n'...")
                continue

        else:
            print("Unknown input, please enter 'y' or 'n'...")
            continue
