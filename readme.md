## [bank security panel](https://github.com/DmitryShvedov88/Comics_pusher "LINK TO THE PROJECT")

This program made for education purpose
The program helps to carry out the access mode in the bank's vault.

### To start a program just do this.

After launching the program, you will see a Web page. There will be several tabs. You will be able to get a list of active passes, a list of all visits to this pass in the vault, as well as information about who is currently in there
    
    python manage.py runserver 0.0.0.0:8000

    example of running:
    System check identified no issues (0 silenced).
    May 08, 2024 - 22:13:24
    Django version 3.2.25, using settings 'project.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CTRL-BREAK.


### How to check
Just click on the available links and get the information you are interested in.

### How to install
Python3 should already be installed.
Use pip (or pip3, if there is a conflict with Python2) to install dependencies.
    
    pip install -r requirements.txt

### environment variables
For the program to function, you will need the following environment variables: 
ENGINE, HOST, PORT, NAME, USER, PASSWORD, INSTALLED_APPS, SECRET_KEY, DEBUG, ROOT_URLCONF, ALLOWED_HOSTS, APP_DIRS, USE_L10N, LANGUAGE_CODE, TIME_ZONE, USE_TZ, DEFAULT_AUTO_FIELD.

You can learn more about the necessary variables in the example .env file

### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.