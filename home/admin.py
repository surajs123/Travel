from django.contrib import admin
from django.contrib.auth.models import auth, User
from .models import destination

# Register your models here.


class userPermission(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_authenticated and request.user.username=='amal':

            return False


        return True



admin.site.register(destination, userPermission)