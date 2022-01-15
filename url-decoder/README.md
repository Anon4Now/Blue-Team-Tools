# ProofPoint URL-Defense Decoder:

I created this tool because I needed a way to decode re-written/encoded URL's from ProofPoint in a GUI-based tool. This was originally designed to be compiled using pyinstaller and run as an exe on Windows OS machines, but it should work as a binary on Linux kernel environments.


The official documentation on ProofPoint's re-write process can be found at this [LINK](https://help.proofpoint.com/Proofpoint_Essentials/Email_Security/User_Topics/Targeted_Attack_Protection/URL_Defense_FAQ's). Also an ❗IMPORTANT note, part of this code is written by a ProofPoint engineer who exposes the decoding process as a Python class that can be used. I took that functionality and incorporated it into this GUI setup, but I do not claim the rights to this code and all attribution goes to the original author. 

[LINK](https://files.mtstatic.com/site_6638/draft_177/2?Expires=1642267881&Signature=fR5vVi5n5ASVK0wJ-NnpitF2lC2EZwlFbbL6kYlpTv-sElldDlWaVaxwkw-6Tgb3-iDlP8JpirA7AFQH2CSxZLKl3eD~GRReT0vptsEYmZVLqp5tCHsHMZA2b3e8yp~u26l1izY~WsKPGPGs63YATbZ4zD5H0eyAmGz5niyQTEY_&Key-Pair-Id=APKAJ5Y6AV4GI7A555NA) to details & author. 
```
__author__ = 'Eric Van Cleve'
__copyright__ = 'Copyright 2019, Proofpoint Inc'
__license__ = 'GPL v.3'
__version__ = '3.0.1'
__email__ = 'evancleve@proofpoint.com'
__status__ = 'Production'
```

## Tool Functionality:

- Will create a GUI that will accept a encoded URL and return the decoded URL
- Can accept copy/paste or manually typed encoded URL


## Tool Requirements:

- To use the default functionality of this tool (watching folders, and creating hashes) a library will need to be installed using pip
    - [tkinter](https://docs.python.org/3/library/tkinter.html)
- This tool needs a ![small](https://user-images.githubusercontent.com/80045938/148561762-9590c4a1-a424-4c7b-a0fb-68190fb7a31c.png) [Python](https://www.python.org/downloads/) interpreter, v3.6 or higher due to string interpolation


## Quick Notes:

- This can be converted to a standalone exe if run on Windows OS
- This should work on Linux, OSX, or Windows OS's
- I have provided a couple of encoded URL examples that can be tested in the 'example_encoded_urls.txt' file


## Using the Tool:

#### Step 1: 
Run the binary or standalone exe to start the tkinter GUI.
![start_ui](https://user-images.githubusercontent.com/80045938/149629964-c123cad5-e4a9-47d0-96df-5323470e7980.gif)


#### Step 2: 
Either copy/paste or manually define the encoded URL.

![input_encoded_url](https://user-images.githubusercontent.com/80045938/149629975-7afb9b54-fde2-4304-b764-3d0cbcdca16e.gif)


#### Step 3: 
Review the output from the GUI.

![decoded_url_output](https://user-images.githubusercontent.com/80045938/149630021-31bc62fc-ba06-4391-a8e9-b864680070c9.jpg)
