# Django Rest Framework

## Configuration and API setup

### HTTP response, request cycle
A REST application as three main parts that are connected to each other: client, api and the database.

<a href="https://images.ctfassets.net/hkpf2qd2vxgx/6LuM2EKyTTq3cziBHcoNQK/d542a85d4c4c9d07a69875ffe7e3b92b/tumblr_inline_mv4xmfwiVv1rtan47.png" alt="http cycle">See the request response cycle</a>

The client makes a request (GET,POST,PUT,DELETE,etc) to the api which uses logic to process the request. If the request requires data then a request is made from the api to the database and a response back to the api. The api takes that data and sends a response to the client. The status of the response is either a 100, 200, 300, 400 or 500. 

### Make a virtual environment
Use this script to create a virtual environment. The virtual environment is used to store all the dependencies needed for the project to work.

```
python3 -m venv venv
```

### Make a gitignore file
Go to a web browser and go to a site that can generate a gitignore file. Toptal is a good site that can generate a gitignore file with options of what you want to be included. To make the gitignore file use the following script:

```
touch .gitignore
```

### Initialize the project with github
Go the root folder in the project and type:

```
git init
```

This will create a .git folder in the root project folder. In order to connect it to github then go through the following commands:

```
git branch -M branchname
gaa
gcmsg 'commit message'
git remote add origin https://www.thegithubrepo
git push -u origin branchname
```

After the initial commit then the remote and local folders are linked. Then you can use the following to push to the github repo:

```
ggpush
```

### Go into the virtual environment
The virtual environment holds all the packages and modules for the project. Use the following to enter the virtual environment:

```
source venv/bin/activate
```

### Start a project
In the root folder type this in the command prompt:

```
django-admin startproject config .
```

This will create a project folder which will hold the configuration files.

### Create env file and insert into the settings file
Go to the config folder and type the following to create a new env file:

```
touch .env
```

In the .env file then add the secret info for the secret key, db and any other secret requirements.

Install the environ module in the virtual environment

```
pip install django-environ
```

Go to the settings.py file in the config folder and at the top import environ.

```
import environ

# Create and retrieve environment variables
env = environ.Env()
environ.Env.read_env()
```

Then when you need to insert a secret value to it the following way:

```
SECRET_KEY = env('SECRET_KEY')
```



