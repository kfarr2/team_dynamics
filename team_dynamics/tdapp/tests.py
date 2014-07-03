from model_mommy.mommy import make
import datetime
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.test import TestCase
from .models import Project, UpdateCheck
from .management.commands.forceupdate import update_table
from .views import force_update

class StdViewTest(TestCase):
    '''
    Tests the standard view for bugs
    '''
    def test_get(self):
        make(Project, _quantity=3)
        response = self.client.get(reverse("std_view"))
        
        self.assertEqual(Project.objects.all().count(),3)
        self.assertEqual(200, response.status_code)


class ForceUpdateTest(TestCase):
    def test(self):
        date = now().replace(microsecond=0)
        make(UpdateCheck, last_update=date)
        response = self.client.get(reverse("std_view"))
        self.assertEqual(response.context['last_updated'].last_update, date)


class UpdateTableTest(TestCase):
    def test(self):
        projects = [
                {"ID": 5, "Name": "foo", "Description": "foo", "StartDate": "2014-07-03 20:42:23+00:00", "EndDate": "2014-07-03 20:42:23+00:00", "AccountName": "foo", "SponsorName": "bar"}
        ]

        update_table(projects)
        self.assertEqual(Project.objects.all().count(), 1)
