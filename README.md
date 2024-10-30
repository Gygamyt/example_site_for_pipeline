# internet-shop

Thx to Kate for sharing this project with me

## Features
- sending emails (order confirmation, user verification)
- authentication (allauth)
- signals
- pagination
- time restriction on ordering

## Installation

```bash
cd src
```

Linux:

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip install requirements.txt
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Run without migrations

```bash
cd src
python manage.py runserver
```

## Testing Emails

To output an account verification message to a console use this in your settings.py file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
To send order confirmations use:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

## Notes

Products images are placed:
```bash
/src/static/media/products_images
```

## Built With
- Django
- Bootstrap
- Gh Actions 
- 