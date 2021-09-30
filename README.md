

# Getting started

## Make a new project
to make a new project use the command in the main folder:

```
python3 manage.py runserver
```

## Create a new app
to make a new app use the command in the main folder:

```
python3 manage.py startapp *appname*
```

## Add files and folders
add a templates folder with a subfolder the same name as the app. create your views and link to the urls. then go to the settings.py file to add the app to the list of installed apps

## Add urls to app and also to main django app
go to the main app urls file and add any parent url that will be used in a sub-app. then go to the sub-app urls and list all the urls that will be used with the parent urls. 

## Create views
create a view that will be used for each url/route. this will be the callback function within the url. the view can be html files that contain the content that will be rendered in the browser. alternatively, views can also be created on the frontend through a framework, library like react, vue, angular

## Make a model
models connect the backend api to the database. each model is a class and has the info for the database table included. django has an orm that is used to define the data types of each column and also when interacting with the database, as opposed to SQL

## Migration / migrate the database 
with the newly made model it can be mapped to a database. a migration will take the info from the model and create it in the database. use this commange to do a migration of the main app folder:

```
python3 manage.py migrate
```

to migrate an individual app then you need to make a migration folder/file and then run the script:

```
python3 manage.py makemigrations 
```

then the script:

```
python3 manage.py migrate
```

## Django ORM
to get to the django ORM shell use:

```
python3 manage.py shell
```

must import the models first and then you can interact with the data/db

### crud operations
#### get all: .all()
#### get first: .all()[0]
#### get by id: .get(id='id')
#### order by: .order_by("fieldname")
#### create/save: .save()
#### update: 
#### delete:  

## django admin 
go to the url admin/ to access the django admin functionality

### make a superuser
use the script:

```
python3 manage.py createsuperuser
```

create username and password that you will use then go back to the browser and login

go to app folder, to the admin.py file. register the model so that you can see in the admin

## Template tags
to make a template tag you use the syntax

python code:

```
{% python code here %}
```

to output data:

```
{{ output data }}
```

## Static pages
static pages are for rendering static pages to the browser. first go to the urls for the main app and import django.contrib.staticfiles.urls from staticfiles_urlpatterns

then at the bottom of the urls file you need to append the urlspatter with the staticfiles urlpatterns that you just imported

go to settings to the static urls and update the static url for the static files. you need to tell django this also by writing:

```
STATICFILES_DIRS = [
    BASE_DIR / "assets"
]
```

create the assets folder in the main app folder and add files like styling, etc that can be used by the static page

to access in the html file use:

```
{% load static %}
```

on the top of the page then use:

```
{% static 'static file' %}
```

to refer to the static file

## Extending templates
using one template multiple times. there can be modularity by extending a base template and then extending it to other templates. Those templates will then use their own content in addition to the base layout/template.

to extend in an html file use:

```
{% extends 'base_template.html' %}
```

to create a block of html:

```
{% block content %}

{% endblock %}
```

in the template you can use:

```
{% block content%}
    html content
{% endblock %}
```

## Url parameters
when requesting a url with dynamic data then a parameter might be used. in order to extract the parameter then in the urls file you need to type:

```
path('<int:id>',views.file)
path('<slug:slug>',views.file)
```

then you can access it in the callback function with the named url parameter

when calling the parameter you can use the following syntax when interacting with the db:

```
def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    payload = {"article":article}
    return render(request,"articles/article_details.html",payload)
```

## Named urls

you can name a url route to link with by using:

```
urlpatterns = [
    path('<slug:slug>',views.article_details,name="details"),
    path('',views.article_list,name="list"), 
]
```

Then in an anchor tag you link it by using the following syntax:

```
<h2><a href="{% url 'articles:details' slug=article.slug %}">{{article.title}}</a></h2>
```

The named url can be used in multiple app by specifying the name of the app in the urls file:

```
app_name = "articles"
```

## Set up media

go to the settings.py file and include the following near the static variables

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

go to the main urls file and include:

```
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

then go to the models.py file and add another field as the thumbnail

```
thumb = models.ImageField(default='default.png',blank=True)
```

then migrate the changes to the db using the makemigrations and migrate scripts

you can go to the django admin to review existing files or create a new one with a thumbnail. just add via the input field and select the media you wish to add.

go to the html file where the media will be located and type:

```
<img src="{{ article.thumb.url }}" alt="{{article.title}}">
```

then it will render to the browser for the user to see.

## User accounts app

create a new users account app:

```
python3 manage.py startapp accounts
```

register this app in the settings.py file

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'accounts',
]
```

go to the accounts folder and make a urls.py file for the routes of accounts

go back to the main app urls.py file and add accounts to the route list

go to the views.py file in the accounts directory and add functions for the views named in the urls.py file

make a template folder with accounts subfolder, then inside the accounts folders make an html template for the accounts views

make a model for the state involved within the accounts routes, views

## User creation form

begin by importing the user creation form:

```
from django.contrib.auth.forms import UserCreationForm
```

then inside the signup function make a variable form and assign the user creation form to it then add to the payload of the request/response to the view

```
def signup_view(request):
    form = UserCreationForm()
    return render(request,"accounts/signup.html",{"form":form})
```

then in the html template then insert a form then add the form payload

```
<form class="site-form" action="/accounts/signup/" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Signup">
</form>
```

the form will show all applicable labels and error handlers that will need styling to make it look user ready

## User sign up form POST and GET

in the signup function in the views.py file add this to the function for a POST request:

```
if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        # log in the user
        return redirect("articles:list")
```

redirect can be added to the shortcuts import

for a GET request then do the following:

```
else:
    form = UserCreationForm()
```

now these users will be seen in the admin portal. these people will not be super user admins

