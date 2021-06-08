from django.contrib import admin
from django.urls import path


from .views import helloView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<name>/', helloView),
]
