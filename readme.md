## [bank security panel](https://github.com/DmitryShvedov88/Bank-security-panel "LINK TO THE PROJECT")

This program made for education purpose
The program helps to carry out the access mode in the bank's vault.

### environment variables
For the program to function, you will need the following environment variables: 
ENGINE, DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, SECRET_KEY, DEBUG, ALLOWED_HOSTS, APP_DIRS.

    ENGINE - specify the database engine and its digital adapter
    DB_HOST - a device that provides client-server services
    DB_PORT - the IP address of the machine on which you are deploying the database
    DB_NAME - that database name
    DB_USER - that user name
    DB_PASSWORD - that password name
    SECRET_KEY - It is used as a cryptographic signature
    DEBUG - database debugging mode
    ALLOWED_HOSTS - A method that checks whether the host matches the settings set by this setting
    APP_DIRS - indicates whether the template engine will search for them inside the application folders in the templates folder

You can learn more about the necessary variables in the env.example file.
Just deploy the virtual environment of the project using the necessary variables, activate it, and you cat start program.

### To start a program just do this.

After launching the program, you will see a Web page. There will be several tabs. You will be able to get a list of active passes, a list of all visits to this pass in the vault, as well as information about who is currently in there
    
    python manage.py runserver 0.0.0.0:8000

    example of running:
    System check identified no issues (0 silenced).
    May 08, 2024 - 22:13:24
    Django version 3.2.25, using settings 'project.settings'
    Starting development server at 'ALLOWED_HOSTS'
    Quit the server with CTRL-BREAK.


### How to check
Just click on the available links and get the information you are interested in.

### How to install
Python3 should already be installed.
Use pip (or pip3, if there is a conflict with Python2) to install dependencies.
    
    python -m venv venv
    venv\Scripts\activate.bat  

### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.