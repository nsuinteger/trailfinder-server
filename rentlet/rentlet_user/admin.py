from django.contrib import admin

# Register your models here.
from rentlet_user.models import RentletUser

admin.site.register(RentletUser)