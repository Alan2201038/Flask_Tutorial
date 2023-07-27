# Flask Tutorial 101
Trying out Python Flask with Git

## Table of Contents
* [First-Timers](#first-time)
    * [Creating your first Virtual Environment](#creating-your-first-virtual-environment)
    * [Installing Dependencies](#installing-dependencies)
    * [Creating your first Flask app](#your-first-flask-app)
    * [Pushing your flask into Git](#git-pushing)
* [Intermediate Flaskers](#second-time)
    * [Cloning GitHub Repos](#git-cloning-jutstu)
    * [Installing Dependencies 2](#installing-dependencies-2)
    * [Runnning your project](#running-it-down)
* [Tips and shitz](#helpful-tips)

## First Time?
This section is for you if you're starting out with Flask, or you forgotten about Flask after your Tri Break.


### Creating your first Virtual Environment

1. To create your first Virtual Environtment (VENV), **first create a folder** for your venv.

    ```
    Folder Name Exaple: Flask
    ```

2. Afterwards, go into your terminal and make sure the **terminal directory is the same route as your folder**.

    ```
    C:/Path/To/Flask>     
    ```

3. Next create your venv using this code. [Make sure your Python is version 3    and not Python 2]

    ```
    > python3 -m venv venv
    ```

    You will see a 'venv' folder being created.
    <br>

    1. If you're using **Windows**, you can use one of these commands to go into your venv.

        ```
        FOR CMD.EXE
    
        >venv\bin\activate.bat
        ```
        ```
        FOR POWERSHELL

        >venv\bin\Activate.ps1
        ```

    2. If you're using **Mac**, you can enter this command in bash.

        ```
        FOR MAC

        $source venv\bin\activate
        ```

Congrats! You have created your first Virtual Environment! :thumbsup:

### Installing Dependencies

1. Now that you have your venv, we can install flask onto it.

    ```
    pip install Flask
    ```

2. Once you installed flask, you can freeze the packages you installed in a .txt for [future use](#installing-dependencies-2).

    ```
    pip freeze > requirement.txt
    ```

Now when you see your **Flask** folder, it will look something like this.

    Flask/
    │
    ├── venv/
    │
    └── requirements.txt

### Your First Flask App
1. First create a python file.

    ```
    app.py
    ```

2. Here is a basic Flask code block.

    ```
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello World!"
    ```

3. To run the application, make sure you activated your venv, your terminal should show you something like this.

    ```
    (venv) C:/Path/To/Flask>
    ```

4. Just type these into your venv terminal and your server will be up and running!

    ```
    >flask run --debug
    ```

### Git Pushing
0. To make this easier for yourself, **create a Github repo first and clone it to your flask folder!!**
<br>

1. Once you have your git repo up and running, you want to add it a .gitignore file in your Flask folder.

    ```
    $ echo venv > .gitignore
    $ echo __pycache__ >> .gitignore
    $ git add .gitignore app.py requirements.txt
    $ git commit -m "Initialize Git repository"
    $ git push
    ```

    "Note that there are some folders that you shouldn’t include in the Git repository, like venv/ and pycache/. " - [Website](https://realpython.com/flask-by-example-part-1-project-setup/) 2023.
    <br>

2. Your Flask Folder will look something like this now.

    ```
    Flask/
    │
    ├── .git/
    │
    ├── venv/
    │
    ├── .gitignore
    ├── app.py
    └── requirements.txt
    ```

And that is it!! Congrats! You have created your First Flask App and pushed it to GitHub!! :smile:

## Second Time!
This section is for clonning other GitHub repos that invloves Flask and how to run them with venv.

### Git Cloning Jutstu

1. **Important Note**: When you git clone a repo to a folder, it **does not** have a venv inside (Most of the time). Make it a habit to [create your own venv](#creating-your-first-virtual-environment) after cloning the repo.
<br>
2. Otherwise here is how to git clone, if you forgotten or smth idk.

       git clone (github repo https)

### Installing Dependencies 2

1. Usually venv has some packages installed. (like Flask for example) Instead of manually installing each package again, we can instead install it one shot with a 'requirement.txt' file if the repo has it.

    ```
    pip install -r requirements.txt
    ```
2. The .txt file might not be called 'requirements.txt.' However, you can see if it's a package list if you check the .txt file manually and you see something like this.

    ```
    blinker==1.6.2
    certifi==2023.5.7
    charset-normalizer==3.1.0
    click==8.1.3
    Flask==2.3.2
    idna==3.4
    itsdangerous==2.1.2
    Jinja2==3.1.2
    MarkupSafe==2.1.3
    urllib3==2.0.3
    Werkzeug==2.3.6
    ```

3. If there is no .txt file at all and you're using a VENV to run your programs. All you can do is check if your project mates what packages are needed and install them. And remember to [freeze](#installing-dependencies) it to prevent installing all manually again!

### Running It Down
To run your Flask program, it's the same. Just do a simple
```
flask run --debug
```
and you're done!

## Helpful Tips
-  To access the webserver on your phone:
  
    1. Make sure your phone and computer are connected to the same wifi.
   
    <br>
    
    2. Find your computer's IP address. (IPv4 Address)
   
        - For Windows, open Command Prompt and type in `ipconfig`.
          
        - For Mac, open Terminal and type in `ifconfig`.
          
        <br>
        
    3. Run your webserver using this command
   
        ```
        flask run --debug -h insert IPv4 Address here
        ```
        
    4. Open your phone's browser and type in the IPv4 Address with the port number.
       
        ```
        IPv4 Address here:5000
        ```
    <br>
    
- Just Google Bro
- If found anything please update here!
