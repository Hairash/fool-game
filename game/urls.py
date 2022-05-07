from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from game.views import index

urlpatterns = [
    path('', index)
] + static(settings.STATIC_URL)

print('* App started')
