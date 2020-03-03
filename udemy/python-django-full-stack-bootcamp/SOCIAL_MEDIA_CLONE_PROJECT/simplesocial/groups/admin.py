from django.contrib import admin
from . imports models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
