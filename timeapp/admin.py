from django.contrib import admin
#from .models import Post,Report
from .models import Post

#admin.site.register(Report)

from django.contrib import admin
from daterangefilter.filters import DateRangeFilter

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = [
        ('range', DateRangeFilter)
    ]

