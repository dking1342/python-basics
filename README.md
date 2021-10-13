# Django Rest Framework: Configuration and API setup

## HTTP response, request cycle
A REST application as three main parts that are connected to each other: client, api and the database.

<a href="https://images.ctfassets.net/hkpf2qd2vxgx/6LuM2EKyTTq3cziBHcoNQK/d542a85d4c4c9d07a69875ffe7e3b92b/tumblr_inline_mv4xmfwiVv1rtan47.png" alt="http cycle">See the request response cycle</a>

The client makes a request (GET,POST,PUT,DELETE,etc) to the api which uses logic to process the request. If the request requires data then a request is made from the api to the database and a response back to the api. The api takes that data and sends a response to the client. The status of the response is either a 100, 200, 300, 400 or 500. 

## Make a virtual environment
Use this script to create a virtual environment. The virtual environment is used to store all the dependencies needed for the project to work.

```
python3 -m venv venv
```

## Make a gitignore file
Go to a web browser and go to a site that can generate a gitignore file. Toptal is a good site that can generate a gitignore file with options of what you want to be included. To make the gitignore file use the following script:

```
touch .gitignore
```

## Initialize the project with github
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

## Go into the virtual environment
The virtual environment holds all the packages and modules for the project. Use the following to enter the virtual environment:

```
source venv/bin/activate
```

## Start a project
In the root folder type this in the command prompt:

```
django-admin startproject config .
```

This will create a project folder which will hold the configuration files.

## Create env file and insert into the settings file
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

## Database setup with postgres

## Set up the django rest framework

## Set up the cors settings

## Settings.py file set up (other)

## Create an apps folder that holds the project apps
Django projects have apps for each aspect of the api. You can create a folder that has all the apps by typing in the root folder:

```
mkdir apps
```

Create an init file in this folder so that it works properly. Go to the apps folder and type:

```
touch __init__.py
```

## Create a new app
When you want to create a new app then create the folder in the apps folder by typing:

```
mkdir appfoldername
```

From the root folder type this to make a new app:

```
python manage.py startapp blogs apps/blogs
```

This runs a command that makes a new app with the app name and the location of where it will be made.

After creating the new app then go into that folder and make a new urls.py file:

```
touch urls.py
```

## Updating settings file for new app
Go to the settings.py file and in the INSTALLED_APPS list add the name of the app:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.blogs',
]
```

Then go to the apps.py file for the new app and make sure that it looks like this for the name variable:

```
class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blogs'
```

## Connect apps via the urls
Go to the config folder and open the urls.py file. Import the include module:

```
from django.urls import path, include
```

Then for the new app make a new path in the urlpatterns list:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blogs/',include('blogs.urls',namespace='blogs')),
    path('api/v1/blogs_api',include('blogs_api.urls',namespace='blogs_api')),
]
```

This now points the routes to the blogs app and the urls.py file within that app folder structure. For the endpoint you can have whatever naming convention you want.

## App url.py config
Start by importing the path module from django and the app views. Then make a list with the name urlpatterns. You can add the app specific routes here with the endpoint, views function or class and the name of the route.

```
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='blogs'), 
    path('something/',Something.as_view(),name='blogs_something')
]
```

The first path is a function and the second one is a class.

## App views.py config
In the views file within the app you will need to add the logic per the route. The logic can be done with a function or class. The function or class will return a response to the client based on the requirement.

```
from django.http.response import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse('django response')
```

## App models.py config for relational db

