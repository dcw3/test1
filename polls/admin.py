from django.contrib import admin

from .models import Question, Zipcode

admin.site.register(Question)
admin.site.register(Zipcode)