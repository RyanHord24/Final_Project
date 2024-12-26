from django.urls import path
from .views import NotebookView, NotebookDetailView

urlpatterns = [
    path('country/', NotebookView.as_view(), name='add_notebook'),
    path('country/<str:country_id>/', NotebookView.as_view(), name='notebook_detail'),
    path('notebooks/<str:country_id>/', NotebookDetailView.as_view(), name='notebook_detail'),
]
