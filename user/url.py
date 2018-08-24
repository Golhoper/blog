from Libraries import *
from user.views import *

urlpatterns = [
    path('login/', login_us, name="login"),
    path('registration/', registration, name="registration"),
    path('reset/', reset, name="reset"),
    path('logout/', logout_us, name="logout")
]
