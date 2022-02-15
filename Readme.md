# Vetchallenge.com Demo My Challenge

This app is django project designed for veterinarians to keep information of pets.
Should expect staff members to check veterinarians' information after registration.
When Staf activates the vet. They can login and add pet information via dashbord. they can remove it.

Demo Here ! -> https://vetdemo.herokuapp.com/

Create a new user and log out and log in with staff user account then go to staff page and confirm your new account
!!
staff user:<br>
username: stafuser<br>
password: stafuser

## Folder structure

```bash
VET/
├─ mainapp/
│  ├─ migrations/
│  ├─tests
│  ├─classic_django_files...
├─ media/
│   ├─ pets
├─ static/
│  ├─ img/
│  ├─ js/
│  ├─ css/
│
├─ template/
│  ├─mainapp/
│  │  ├─user/
│  ├─userpage/
│
├─ userpage/
├─ vet/
├─ db.sqlite3


```

## Installation

github clone and github download zip

## Dependencies Install

```bash
pip install requirements.txt

```

## Requirements

```bash
asgiref==3.5.0
cycler==0.11.0
Django==3.2.8
fonttools==4.29.1
greenlet==1.1.2
gunicorn==20.1.0
kiwisolver==1.3.2
matplotlib==3.5.1
numpy==1.22.2
packaging==21.3
Pillow==9.0.1
pyparsing==3.0.7
python-dateutil==2.8.2
pytz==2021.3
six==1.16.0
SQLAlchemy==1.4.31
sqlparse==0.4.2
whitenoise==6.0.0

```

and running

````

## Usage //runing is here!

```python
python manage.py runserver

````

## Usage Test

```python
python manage.py test mainapp
python manage.py test userpage

```

## For Heroku Deployment

```python

1-requirements.txt oluştur.
2-Procfile oluştur -> web: gunicorn vet.wsgi  <settings dosyasının olduğu app>.wsgi
3-runtime.txt ->python-3.8.8
4-ALLOWED_HOSTS =[]-> your host address and localhost address
4-settings dosyası:
Debug=False
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

```

## Next Version

Since I'm thinking of submitting the project, I'm thinking of adding a few missing and missing processes in the next version:<br>
I forgot pages 1-404<br>
2-html ,css should be developed<br>
3-owners detail page<br>
4-forms clean functions are missing<br>
5-email password reset<br>
6- registration with google accounts<br>
7-login and similar decalators are missing<br>

## For Development

1-Debug=True
2-ALLOWED_HOSTS=... delete addresses in l.
3-STATIC_ROOT =comment line

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
