from django.urls import path

import shop
from . import views

app_name = 'search_app'


urlpatterns=[

    path('',views.SearchResult,name='SearchResult'),
]
