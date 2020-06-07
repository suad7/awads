from django.contrib import admin
from .models import Project,Profile,Comments,Review
# Register your models here.

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Review)

