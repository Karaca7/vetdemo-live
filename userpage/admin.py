from django.contrib import admin
from userpage.models import Pet,PetOwner

# Register your models here.

admin.site.register(Pet)
admin.site.register(PetOwner)
