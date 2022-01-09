from watchdog import Watchdog
from user_cli import GetUserOptions
from hash_generator import HashGenerator

if __name__ == '__main__':

    while True:

        userInput = input("Would you like to start watching a folder? y/n")

        if userInput == 'y':

            # show time left to download file on CLI
            print(f'Seconds Left to Download File...\n')
            for i in range(30, -1, -1):
                if not True in currentState:  # UPDATE THIS CLASS VAR FROM IMPORT
                    if i == 0:
                        sys.stdout.write(f'No File Given')
                        sys.stdout.flush()
                        time.sleep(1)
                    else:
                        sys.stdout.write(str(i) + f' ')
                        sys.stdout.flush()
                        time.sleep(1)

                else:
                    print(f'File seen - generating hashes...\n')
                    sys.stdout.flush()
                    break

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
