from Libraries import *
from articles.views import *

urlpatterns = [
    path('', main_us, name="main"),
    path('admin/', create_art, name="admin"),
]
