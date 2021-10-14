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

Add environ to the installed apps.

```
INSTALLED_APPS = [
    ...
    'environ',
    ...
]
```

Then when you need to insert a secret value to it the following way:

```
SECRET_KEY = env('SECRET_KEY')
```

## Database setup with postgres
Open the env file and enter the secret info the for the postgres server:

```
ENGINE=django.db.backends.postgresql_psycopg2
NAME=database_name
USER=database_user
PASSWORD=database_password
HOST=localhost or database_host
PORT=5432
```

Go to the settings file and enter the config info for the database:

```
DATABASES = {
    'default': {
        'ENGINE':env('ENGINE'),
        'NAME':env('NAME'),
        'USER':env('USER'),
        'PASSWORD':env('PASSWORD'),
        'HOST':env('HOST'),
        'PORT':env('PORT'),
    }
}
```

In the virtual environment use pip to install psycopg2

```
pip install psycopg2
```

Go to your terminal and go to the postgres terminal environment.

```
psql
```

To create the database:

```
CREATE DATABASE blogs;
CREATE USER database_user WITH ENCRYPTED PASSWORD 'database_password';
GRANT ALL PRIVILEGES ON DATABASE blogs TO database_user;
```

To check and see if the database is there then type \d to see all the databases.

## Set up the django rest framework
Go to your virtual environment and install django rest framework:

```
pip install djangorestframework
```

Add django rest framework to your installed apps within the settings.py file:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Insert this new variable into the settings.py file:

```
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

## Set up the cors settings
First use pip to install the cors header module to your virtual environment

```
pip install django-cors-headers
```

Then go to the settings.py file to the installed apps list and include it.

```
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

Go to the settings.py file and add the following variables

```
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ORIGIN_ALLOW_ALL = True
```

This will help with the methods and who can access the api. Then go to the middleware and add cors to it.

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Make sure to put the corsheader near the top as middleware works from the top to the bottom.

## Settings.py file set up (other)
To set up the media files and path then at the bottom of the settings.py file add the following and make sure that the os module in imported:

```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

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
    path('api/v1/blogs/',include('apps.blogs.urls')),
    path('api/v1/blogs_api',include('apps.blogs_api.urls')),
]
```

This now points the routes to the blogs app and the urls.py file within that app folder structure. For the endpoint you can have whatever naming convention you want.

## App url.py config
Start by importing the path module from django and the app views. Then make a list with the name urlpatterns. You can add the app specific routes here with the endpoint, views function or class and the name of the route.

```
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('',views.homepage,name='blogs'), 
    path('something/',Something.as_view(),name='blogs_something')
]
```

The first path is a function and the second one is a class.

If you want to have parameters in the route then you can make a path like this:

```
urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='blog'),
    path('',PostList.as_view(),name='blogs'),
]
```

The first route here shows <int:pk> which gives the name of the parameter and the data type. The data type can be str, slug, int, etc.

## App views.py config
In the views file within the app you will need to add the logic per the route. The logic can be done with a function or class. The function or class will return a response to the client based on the requirement.

```
from django.http.response import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse('django response')
```

To make a class then use the following sytax:

```

```

## App models.py config for relational db
Start by importing any modules that you may require. Then create a class which will represent a table in the database.

```
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

The columns of the table will be listed then a function __str__ will be included so that the query being sent back will be in a readable format.

You can include classes inside the parent class and other variables, etc needed. The columns will have features similar to an sql db setting. You can add a meta class if you want to do anything special with the table. This is an example of a more elaborate table:

```
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250,unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=10,choices=option,default='published')    
    objects = models.Manager()
    postobjects = PostObjects()
    
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
```

After you are satisfied with the table and contents within then you will need to work on migrating this model into the actual database. You will need to enter two scripts. The first is a staging area:

```
python manage.py makemigrations
```

The second will create, update, delete, etc the table/s in the database

```
python manage.py migrate
```

This should create a new folder within your app called migrations. You can check the files inside for the migrations that have taken place when you run these scripts.

You can also go to the psql terminal and query the database to see all the tables that have been added, edited, etc. To do this do this:

```
# This will change the database being shown
\c blogs 

This will show all the tables
\d
```

## App models.py config for nosql db

## Config admin to show app models
Go to the admin.py file inside the app folder structure. Inside the admin file you will need to register the model of this app by doing the following:

```
from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
```

The models need to be made first so that they can be imported. 

## Create superuser for admin
To make a super user for the admin app then go to the root folder and type:

```
python manage.py createsuperuser
```

You will enter a username, email and/or password. This will be your credentials to use the admin portal. Now you can go to the url localhost/admin/ and log in after you start running the server.

## Run the server
In order to run the server you can type in:

```
python manage.py runserver
```

This will create a server to access typically on port 8000. You can access this now and use as per your needs.

If there are any errors blocking the server from running then this will show and you will need to clear these errors before you can use the server.

