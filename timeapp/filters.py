from django.contrib.auth.models import User
import django_filters

from django_filters import DateRangeFilter,DateFilter

from django_filters.widgets import RangeWidget


from .models import Post

class PostFilter(django_filters.FilterSet):
    #start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    #end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    #date_range = DateRangeFilter(field_name='date')
    date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))


    class Meta:
        model = Post
        #fields = ['start_date', 'end_date','date_range','Date']
        fields = ['date']
        order_by = ['date']
