from django.contrib import admin
from .models import Artists, Albums, Tracks
# Register your models here.

admin.site.register([Artists, Albums, Tracks])