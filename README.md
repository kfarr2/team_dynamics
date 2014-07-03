# Team Dynamix Project Database

##Install
    
    virtualenv-2.6 --no-site-packages .env
    source .env/bin/activate
    pip install -r requirements.txt

Create a local copy of the settings, and configure the SECRET_KEY, BEID and WEB_SERVICES_KEY 
    
    cd team_dynamics/settings/local.py.template team_dynamics/settings/local.py
    vi team_dynamics/settings/local.py

Sync the DB
    
    ./manage.py syncdb
    ./manage.py migrate

##Management command

In order to update the database, use the management command 'forceupdate'
    
    from django.core.management import call_command
    call_command('forceupdate')
