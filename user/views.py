import url_names

from Libraries import *
from user.functions import *
from user.models import SecretWords


def login_us(request):
    if request.method == "POST" and not request.user.is_authenticated:
        name = request.POST["username"]
        pasw = request.POST["password"]

        if len(name) > 0 and len(pasw) > 0:
            user = authenticate(username=name, password=pasw)
            if user is not None:
                group = User.objects.get(username=name).groups.get()
                if user.is_active == 1 and str(group) == 'users':
                    login(request, user)
                    return redirect('main')
    return render(request, url_names.Names.login)


def registration(request):
    if request.method == "POST":
        name = request.POST["username"]
        pasw = request.POST["password"]
        email = request.POST["email"]
        f_name = request.POST["first_name"]
        l_name = request.POST["last_name"]
        secret_word = request.POST["secret word"]

        if reg_fields(name, pasw, email,f_name, l_name):
            user = User.objects.create_user(username=name, email=email, password=pasw,
                                            first_name=f_name, last_name=l_name, is_active=1,
                                            is_superuser=0, is_staff=0)
            group = Group.objects.get(name="users")
            User.objects.get(username=user).groups.add(group)
            user.save()
            SecretWords.objects.create(id_user=user, keyword=secret_word)
            return redirect('main')
        else:
            return render(request, url_names.Names.registration)
    else:
        return render(request, url_names.Names.registration)


def logout_us(request):
    logout(request)
    return redirect('main')


def reset(request):
    if request.method == "POST":
        name = request.POST["username"]
        pasw = request.POST["new_password"]
        word = request.POST["keyword"]

        user = User.objects.get(username=name)
        keyword = SecretWords.objects.get(id_user_id=user).keyword

        if word == keyword:
            user.set_password(pasw)
            user.save()
            return redirect('login')
    return render(request, url_names.Names.reset)