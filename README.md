# articuno-webapp
This a simple Django + PostgresSQL login/signup app built as an assignment from Articuno Coding LLP.

## **Deployed Website**
---

**Branch        :** `deploy`

**Deployed on   :** `heroku` 

**Database      :** `PostgreSQL DB` 

**URL           :** [articuno-webapp.herokuapp.com](https://articuno-webapp.herokuapp.com/)

### **CREDENTIALS FOR ADMIN DASHBOARD**

**URL           :**  [Admin Dashboard](https://articuno-webapp.herokuapp.com/admin/)

**Username      :** admin

**Password      :** pass@1234


## **SCREENSHOTS**
+ Home 
  
![home](https://github.com/MAX-EINSTEIN/articuno-webapp/blob/deploy/pictures/home.png?raw=true)

+ Login
  
![login](https://github.com/MAX-EINSTEIN/articuno-webapp/blob/deploy/pictures/login.png?raw=true)

+ Sign Up 
  
![signup](https://github.com/MAX-EINSTEIN/articuno-webapp/blob/deploy/pictures/signup.png?raw=true)

+ DashBoard 
  
![dashboard](https://github.com/MAX-EINSTEIN/articuno-webapp/blob/deploy/pictures/dashboard.png?raw=true)

+ Admin 
  
![admin-login](https://github.com/MAX-EINSTEIN/articuno-webapp/blob/deploy/pictures/admin-login.png?raw=true)

<br/>

![admin-panel](https://github.com/MAX-EINSTEIN/articuno-webapp/blob/deploy/pictures/admin-panel.png?raw=true)

<br/><br/>

## **Development Environment**
---

**Branch        :** `main`

**Developed on  :** `Ubunutu 20.04 WSL + Windows 11`

**Database      :** `SQlite3` *(only meant for dev enviroment, PostgresSQL used in production)*

### **BUILD INSTRUCTIONS**

+ Clone the repo and cd into it
```
git clone https://github.com/MAX-EINSTEIN/articuno-webapp.git
cd articuno-webapp
```

+ Create a virtual environment and activate it
```
python -m venv .venv
source .venv/bin/activate (On Ubunutu)
.venv/Scripts/activate (On Windows)
```

+ Install the dependencies from requirements.txt
```pip install -r requirements.txt```

+ Make Migrations and migrate 
```
python manage.py makemigrations
python manage.py migrate
```

+ Create a Super User
```
python manage.py createsuperuser
```
You can use the credentials created for the user to login to the admin dashboard.

+ Run the app
```
python manage.py runserver
```