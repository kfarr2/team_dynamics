import json
import time, datetime
import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc
from team_dynamics.tdapp.models import Project, UpdateCheck

class Command(BaseCommand):
    '''
    Forces an update on the database
    '''
    def handle(self, *args, **options):
        return get_info() 

# Static specified attributes
HIGHLIGHTED_PROJECT_ATTRIBUTE_ID = 9279
HIGHLIGHTED_PROJECT_ATTRIBUTE_VALUE_ID = 21848

default_kwargs = {
        "headers": {"content-type": "text/json"},
        "cookies": {}
        }


def post(endpoint, **kwargs):
    '''
    Returns an http post object to calling function using the requests module
    '''
    return requests.post("https://pdx.teamdynamix.com/TDWebApi/api/" + endpoint, **dict(default_kwargs.items() + kwargs.items()))


def get_projects():
    '''
    gets a json object using the get function defined above. returns to calling function
    '''
    # get the login cookie
    r = post('auth/loginadmin', data = json.dumps({"BEID": settings.BEID, "WebServicesKey": settings.WEB_SERVICES_KEY}))
    # save the authentication cookie for future requests to the API
    default_kwargs['cookies'] = r.cookies
    r = post("projects/search", data=json.dumps({"CustomAttributes": [{"ID": HIGHLIGHTED_PROJECT_ATTRIBUTE_ID, "Value": HIGHLIGHTED_PROJECT_ATTRIBUTE_VALUE_ID}]}))
    return r.json()


def get_info():
    """
    calls the team dynamics api to check projects and update the database
    """
    update = UpdateCheck()
    update.last_update = datetime.datetime.utcnow().replace(microsecond=0,tzinfo=utc)
    projects = get_projects()                              
    update_table(projects)
    update.save()


def update_table(projects):
    '''
    Takes a json object and matches its variables and attributes with those in the
    database. It then modifies current projects and adds new ones.
    '''
    for data in projects:                       
        proj = Project()
        proj.project_id = data['ID']
        proj.name = data['Name']
        proj.description = data['Description']
        proj.start_date = data['StartDate']
        proj.end_date = data['EndDate']
        proj.account_name = data['AccountName'] or 'N/A'
        proj.sponsor_name = data['SponsorName'] or 'N/A'
        proj.save()
