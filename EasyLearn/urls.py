from django.contrib import admin
from django.urls import path
from quiz.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('subject/', subject_list),
    path('subject/<str:subject>/', question_list)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
