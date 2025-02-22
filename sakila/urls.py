from django.urls import path, re_path
from sakila import views


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),
    # re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),
    path('film/modify', views.film_modify, name='film_modify'),
    path('customer/', views.CustomerListView.as_view()),
    path('customerAjax', views.CustomerAjaxView.as_view()),
    path('customerAjaxCreate', views.CustomerAjaxCreateView.as_view()),
    # path('staff/', views.list_staff, name='staff'),
]
