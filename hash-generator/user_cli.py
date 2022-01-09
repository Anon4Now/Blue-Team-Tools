import optparse


class GetUserOptions:
    parser = optparse.OptionParser()

    @staticmethod
    def setOptions():

        GetUserOptions.parser.add_option("-f", "--folder", dest="folder",
                                         help="Path for watchdog to monitor for changes")  # generate options for args
        GetUserOptions.parser.add_option("-v", "--virusTotal", dest="virusTotal",
                                         help="Check the SHA256 hash against Virus Total hash DB")  # generate options for args

        parsingInput = GetUserOptions.parser.parse_args()
        return parsingInput

    def checkOptions(self):
        (options, args) = self.setOptions()

        if not options.folder:  # provide inline error-handling if needed args are not provided
            GetUserOptions.parser.error("[-] Please specify an interface, --help for more info")
        else:
            return options

