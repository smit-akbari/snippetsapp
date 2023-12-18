from django.urls import path
from .views import SnippetDetail, SnippetList
from . import views


urlpatterns = [
    path('Snippetapp/', SnippetList, name='SnippetList'),
    path('Snippetapp/<int:id>/', SnippetDetail, name='SnippetDetail'),
    path('snippet/form/', views.snippet_form, name='snippet_form'),
]
