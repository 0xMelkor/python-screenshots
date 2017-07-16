# python-screenshots
Ever needed to get screenshots when your keyboard is disabled? Now you can with this simple script.
Use your dx mouse button to get screenshots and put them in a folder of your choice 

# Prerequisites
* **Operative System:** Windows OS
* **Python interpreter:** Python 2.7 64 bit version
* **Python tools:** pip, virtualenv

## Operative System
This simple python app has platform dependent requirements. This version of the app only supports Windows machines 

## Python interpreter
The app has been developed in Python 2.7. Please download the 64 bit interpreter from the official [Python repository](https://www.python.org/download/releases/2.7/).
After installation is completed be sure you add `python.exe` and the `Scripts/` folder to your PATH environment variable. 
For instance, if you installed Python under **C:\Python27**, add the following string to your PATH variable:
`C:\Python27;C:\Python27\Scripts;`
This will ensure you will be able to run python and pip from any directory through a command prompt


## Python tools
You are gonna need two standard python tools to run your script:
* **pip:** will istall all script's dependencies listed in the  `requirements.txt` file
* **virtualenv:** will provide a sandboxed python environments to run your script. All dependencies will be installed in this sandbox leaving the global python packages directory cleaned

### pip
This tool is already installed and can be found under the `Scripts/` folder of your python installation.

### virtualenv
Virtualenv is a python package that you can install through pip. Open a terminal and run
`pip install virtualenv`

# Configure and run the script
## Configure 
You should follow these steps:
1. Download the project from this repo
2. Open a terminal
3. `cd` into the project folder
4. Create a virtualenv `virtualenv dirname`, this will create a python2.7 virtualenv under the `dirname` folder
5. Install app dependencies with `pip install -r requirements.txt`

## Run
You should follow these steps:
1. Open a terminal
2. `cd` into the project folder
3. Activate the virtualenv by running`path-to-your-virtualenv/Scripts/activate`
4. Run the command `python pyscreen.py destdir` where destdir is the folder where your screenshots will be placed
5. You can kill the script by closing the terminal

### Stealth mode
If you want to run your script in background without an open terminal you can:
Run `pythonw pyscreen.py destdir` to launch the script and `taskkill /f /im pythonw.exe` to terminate it 

