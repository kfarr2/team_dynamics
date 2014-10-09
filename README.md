# Team Dynamix Project Database

##Install
    
    virtualenv-2.6 --no-site-packages .env
    source .env/bin/activate
    pip install -r requirements.txt

Create a local copy of the settings, and configure the following values:

- SECRET_KEY
- BEID
- WEB_SERVICES_KEY
- HIGHLIGHTED_PROJECT_ATTRIBUTE_ID
- HIGHLIGHTED_PROJECT_ATTRIBUTE_VALUE_ID

Ask the repo manager for the specific values.

    cp td/settings/local.py.template td/settings/local.py
    vi td/settings/local.py

Sync the DB
    
    ./manage.py syncdb

##Management command

In order to update the database, use the management command 'forceupdate'

    python manage.py shell
    from django.core.management import call_command
    call_command('forceupdate')
    
or

    ./manage.py forceupdate
