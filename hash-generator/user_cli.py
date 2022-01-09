import sys, time

from watchingdog import Watchdog


class GetUserOptions:
    fileDetected = False

    @staticmethod
    def startWatchingPath():

        path = input(
            "[+] Folder to be monitored, default is Downloads [enter file path or enter 'd' for default]? >> ")

        if path == 'd':
            path = 'C:/Users/tutko/Downloads'
            return path
        else:
            pass  # update this to pull the folder based on input (i.e. Documents)

    @staticmethod
    def countDownToDownload():
        for i in range(45, -1, -1):
            if not Watchdog.eventCheck:
                if i == 0:
                    sys.stdout.flush()
                    # sys.stdout.write(f'\r[-] No file detected, returning to start...')
                    return

                else:
                    sys.stdout.write("\r" + str(i))
                    sys.stdout.flush()
                    time.sleep(1)

            else:
                print(f'\r[+] File seen - generating hashes...\n')
                sys.stdout.flush()
                return True

    @staticmethod
    def useVirusTotal():

        vt = input("Would you like to check the SHA256 hash against VirusTotal DB [y/n]? >> ")

        if vt == 'y':
            return True
        elif vt == 'n':
            return False
        else:
            return

    @staticmethod
    def stopWatching():
        exit()
