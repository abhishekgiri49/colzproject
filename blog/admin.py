from django.contrib import admin
from blog.models import Destination
from .models import UserVisited

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'trekking_type', 'accomodation_type', 'action']
admin.site.register(Destination, DestinationAdmin)


class UserHistoryAdmin(admin.ModelAdmin):
	list_display = ['user', 'destination']
admin.site.register(UserVisited, UserHistoryAdmin)
