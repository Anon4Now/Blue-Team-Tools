### Hash Generator

I created this tool because I wanted an easier way to evaluate downloads that I was making online. 

A lot of good sites provide the hashes that are attributed to their offical copy of the product, however that hash is only as good as the user who recreates it after download. This tool will automate that process of generating the hashes and makes it easier to compare to the hash value on the download site. Additionally this tool has a module that will call a VirusTotals API and check to see if a this hash was evaluated before, and if so it will return those findings.


## Tool Functionality:

- Will use a "watchdog" function to monitor a path defined by the user, it will default to the OS's "Download" folder
- Will generate SHA256, SHA1, and MD5 hashes for a file, this is done because some sites provide only one of those options
- Can provide the ability to take the SHA256 hash and check VirusTotal's scanned database of details (read on for how to enable this functionality)

## Tool Requirements:

- To use the default functionality of this tool (watching folders, and creating hashes) a couple of modules will need to be installed
    - watchdog
    - etc
    - etc
- To use the VirusTotal API functionality, it will require an VT account and API key
    - Use this link to learn more about this process (it's easy honestly)
    - Afterwards progress to IMPORTANT section below for information about what to do with the API key
- Lastly this tool needs a Python interpreter, v3.6 or higher due to string interpolation


## Quick Notes:

- This can be converted to a standalone exe if run on Windows OS
- This tool will work regardless of whether the API functionality is set-up, the prompt to run against VT will not appear
- This should work on Linux, OSX, or Windows OS's

## IMPORTANT:

This tool will hide the prompt to take the generated SHA256 hash unless the user has created a .env file in the same directory as the source files. This is done to prevent the user from attempting to hard code their API credentials into the code, and to do it the secure way through leveraging environment variables.

Obviously I cannot stop anyone from taking that route if that really want, but I would strongly suggest against it. Creating and using environment variables for this tool is easy. For more information on how to create a .env file, use this LINK.

Once you have created the file in the correct directory update the file with the variables below, reference the VirusTotal's API docs for more info:
```
# Development settings
API_ENDPOINT=https://www.virustotal.com/api/v3/files/
API_KEY="x-apikey"
API_KEY_VAL="<API_KEY>"
```
At this point you are done, and the prompt "*Would you like to check the SHA256 hash against VirusTotal DB? [y/n] >>*" should appear after you generate hashes.


## Using the Tool:

#### Step 1: Run the binary with a Python interpreter or as a standalone exe


#### Step 2: Download the wanted file, the program will identify the file downloaded and generate SHA256, SHA1, and MD5 hashes


#### Step 3: !IMPORTANT For this option to be presented to the user, a .env file will need to be present
