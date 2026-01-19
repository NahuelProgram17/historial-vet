from django.urls import path
from .views import (
    ClinicalRecordListView,
    ClinicalRecordDetailView,
    ClinicalRecordCreateView,
    ClinicalRecordUpdateView,
    ClinicalRecordDeleteView,
)

app_name = 'pages'

urlpatterns = [
    path('', ClinicalRecordListView.as_view(), name='list'),
    path('create/', ClinicalRecordCreateView.as_view(), name='create'),
    path('<int:pk>/', ClinicalRecordDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', ClinicalRecordUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ClinicalRecordDeleteView.as_view(), name='delete'),
]
