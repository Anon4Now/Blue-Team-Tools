import getpass
import platform
import sys, time

from watchingdog import Watchdog


class GetUserOptions:
    fileDetected = False

    @staticmethod
    def startWatchingPath():

        osName = platform.system()
        username = getpass.getuser()

        defaultPath = input("[+] The default path to monitor is Downloads, do you want keep this? [y/n] >> ")

        if defaultPath == 'y':
            if 'Windows' in osName:
                path = f'C:/Users/{username}/Downloads'
                return path
            elif 'Linux' in osName:
                path = f'/home/{username}/Downloads'
                return path
        elif defaultPath == 'n':
            path = input("[+] Enter path to folder to monitor (remove quotations '\"')? >> ")
            if '\\' in path:
                path = path.replace("\\", "/")
            return path

    @staticmethod
    def countDownToDownload():
        for i in range(45, -1, -1):
            if not Watchdog.eventCheck:
                if i == 0:
                    sys.stdout.flush()
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

        vt = input("Would you like to check the SHA256 hash against VirusTotal DB? [y/n] >> ")

        if vt == 'y':
            return True
        elif vt == 'n':
            return False
        else:
            return

    @staticmethod
    def stopWatching():
        exit()
