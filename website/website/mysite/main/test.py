from django.test import TestCase
from main.models import Parlour
from datetime import datetime
# Create your tests here.
class ParlourTest(TestCase):
	def setup(self):
		Parlour.objects.create(Parlour_name="Zoonix",
			tutorial_content="Parlor Management System", date=datetime.now())
	def test_ORM(self):
		p = Parlour.objects.get(Parlout_name="Zoonix")
		self.assertEqual(p.parlour_name,"Zoonix123")