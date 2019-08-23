from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # re_path(r'^app.*\.html', views.gentella_html, name='gentella'),
    # re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('app', views.index, name='index'),
    # path('', views.index, name='index'),
]
