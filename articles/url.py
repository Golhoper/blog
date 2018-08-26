from Libraries import *
from articles.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_us, name="main"),
    re_path('^delete/(?P<id>\w+)/$', delete_art, name="delete"),
    re_path('^change/(?P<id>\w+)/$', change_art, name="change"),
    # path('profile/',TemplateView.as_view(template_name='profile.html')),
    # path('saved/', SaveProfile, name='saved'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
