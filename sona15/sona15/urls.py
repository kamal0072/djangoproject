
from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SchoolView.as_view(),name='home'),
    path('list/',views.SchoolListView.as_view(),name='list'),
    path('deatil/<int:pk>',views.SchoolDetailView.as_view(),name='deatil'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.SchoolDeletView.as_view(),name='delete'),
    path('schoolform/',views.SchoolFormView.as_view(),name='schoolform'),
]
