

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

