# Bangazon API

## Overview
This is a Django REST Framework API developed in support of this project: . Similar to all the other projects associated with the Bangazon platform, this API provides endpoint access to Bangazon resources, including customers, products, orders, product types, etc. Authentication is required if attempting to view in the browser. Instructions for viewing from the admin panel are below.

## Setup
Create a directory on your computer where you will store the project files. 
Navigate to that directory.
Clone or download this repo.
Navigate to the `api` folder and check if there is a `migrations` folder inside. If so, you may (optionally) want to delete these and run them anew by running `rm -rf migrations` and then running `python manage.py makemigrations api` in the root folder. After that, you can run `python manage.py migrate` to ensure that the db.sqlite3 file is up to date. After that, you'll need to launch your server using `python manage.py runserver` and navigate to `localhost:8000` in your browser. The API Root view should be exposed, but you may not see any information or a message indicating that you are not authenticated. This is expected behavior. There are two options: creating a superuser and viewing the API from the admin panel by running `python manage.py createsuperuser`, following the prompts, and then using those credentials to login at `localhost:8000/admin`. You should then be able to see all the tables and associated data. Another method to view the API without creating an admin user would be to open the `setting.py` file in the root of the project and removing temporarily the authentication required code under `REST_FRAMEWORK`, lines 41-43 of the code on that page. Simply commenting that out should remove authentication and allow you to view all endpoints from `localhost:8000`. 

## Contributors
- Whitney Cormack
- Abby Fleming
- Sam Phillips
- LaDonna Sales
- Richard Whitfield
