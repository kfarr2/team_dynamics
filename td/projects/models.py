from django.db import models

class Project(models.Model):
    '''
    Responsible for database management. The values in this model are
    used to compare information from the API to determine what to add to the database.
    '''
    project_id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=255)            
    description = models.TextField()     
    start_date = models.DateTimeField()       
    end_date = models.DateTimeField()         
    account_name = models.CharField(max_length=255)     
    sponsor_name = models.CharField(max_length=255)     

    class Meta:
        db_table = 'tdapp_project'
        ordering = ["name"]


class UpdateCheck(models.Model):
    '''
    Responsible for the table showing the most recent updates.
    '''
    last_update = models.DateTimeField(primary_key=True)

    class Meta:
        db_table = "tdapp_updatecheck"

