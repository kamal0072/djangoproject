
from django.contrib import admin
from django.urls import path,include
from enroll import views
from enroll.views import delete_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_time,name='home_time'),
    # path('',views.StudentListView.as_view(),name='home_time'),
    path('create/',views.create_view,name='create'),
    path('list/',views.list_view,name='list'),
    path('detail/<int:id>',views.detail_view,name='list'),
    path('detail/<int:id>',views.detail_view,name='list'),
    path('update/<int:id>',views.update_view,name='update'),
    path('<id>/delete', delete_view ),
    # path('home/',include('enroll.urls')),
    # path('home2/',include('enroll.urls')),
]
