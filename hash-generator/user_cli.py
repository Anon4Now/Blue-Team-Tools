import optparse


class GetUserOptions:
    parser = optparse.OptionParser()

    @staticmethod
    def setOptions():

        GetUserOptions.parser.add_option("-p", "--path", dest="path",
                          help="Path for watchdog to monitor for changes")  # generate options for args
        GetUserOptions.parser.add_option("-vt", "--virusTotal", dest="virusTotal",
                          help="Check the SHA256 hash against Virus Total hash DB")  # generate options for args

        parsingInput = GetUserOptions.parser.parse_args()
        return parsingInput

    def checkOptions(self):
        (options, args) = self.setOptions()

        if not options.interface:  # provide inline error-handling if needed args are not provided
            GetUserOptions.parser.error("[-] Please specify an interface, --help for more info")
        elif not options.mac_choice:
            GetUserOptions.parser.error("[-] Please specify a MAC address flag, --help for more info")
        else:
            return options
