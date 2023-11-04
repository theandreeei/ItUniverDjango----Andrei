from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('pet', views.pet),
    path('fullname', views.fullname),
    path('place', views.place),
    path('years_old', views.years_old),
    path('education', views.education),
    path('hobby', views.hobby),
    path('else_about_me', views.else_about_me),
    path('films', views.films),
    path('remove/<int:number>', views.remove),
    path('completed', views.completed, name='completed'),
    path('info/task_<int:number>', views.info)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
