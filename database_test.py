import django
django.setup()

from submit_url.models import Companies # import will be different depending on script location

list1 = Companies(name="apple", sector_id=5, sector="somthing")
list1.save()
