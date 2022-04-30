# Bookstore Web App

Bookstore is a small online book store management system developed in Django.

* Users: 
    * Admin
        * Add / Remove categories, subcategories, suppliers.
    * Supplier
        * Add Book 
    * Customer
        * View Book
        * Add / remove book to and from cart
        * View Cart 
        * Place order
* Books:
    * Categories > Sub Categories > Books
    * Filter Books based on:
        * Title
        * Author or Title
        * Date published
        * ISBN 
        * Categories or subcategories
        * Price
 
## Installation
* Follow these to install and set-up development server locally.

### Prerequisites
* Make sure Python 3.8+, pip, git are installed on your system. 
    * Clone this repository:
    
```git clone https://github.com/kill-gear/django-bookstore.git```

Once cloned, create a virtual environment in the root directory of this repository:

```python3 -m venv venv-bookstore```

Then activate this virtual environment using:

```source ./venv-bookstore/bin/activate ``` 

For Windows, check venv documentation for exact usage
Now install the dependencies using the following command:

```python3 -m pip install -r requirements.txt```


### Server Configuration

* There's a file named ```local_settings.py``` in ```django-bookstore/bookstore/``` modify the relevant keys and config in the file and save. 
    
    * Get ```SECRET_KEY``` 
        * A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value. [Django docs](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key)
        * Default: ```''```
        * Generate SECRET_KEY:
            * ``` python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"```
            * Copy this key and paste in the ```local_settings.py``` 
        * This is a one time step, do not rotate your key.

    * You can leave ```DEBUG=True``` and ```ALLOWED_HOSTS=[]``` empty, for development server. 

### Set-up DB (SQLite3)
* Make Migrations - It is responsible for creating new migrations based on the changes you have made to your models.

    * ```python3 manage.py makemigrations```
* Migrate - It is responsible for applying migrations, as well as unapplying and listing their status.

    * ```python3 manage.py migrate```
* Initially it is required to make & set-up DB but whenever you edit ```models.py``` run above commands.

### Create superuser for Django Admin
* It's needed to create a user account that has control over everything on the admin site i.e. ```view/add/update/delete```  data in all models.
```
python3 manage.py createsuperuser
```
    Set username, email and password and go to below mentioned URL:
  
```127.0.0.1:8000/admin``` (Default) to log-in and view the models and DB.

### Start the Development Server
And we're done! Time to start the web server and see if our website is working!

```python3 manage.py runserver```

* Add Categories, Subcategories, Books 
* You should see something like this.
![Example Twitter Top Tweets WebApp](https://www.dl.dropboxusercontent.com/s/cd85j4lwjnt66em/bookstore.png)

***
This project is deployed on pythonanywhere, [check out!](https://djangobookstore.pythonanywhere.com)
***
