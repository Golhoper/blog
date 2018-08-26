import url_names
from Libraries import *
from articles.models import Articles
from .forms import ProfileForm


def delete_art(request, id):
    art = Articles.objects.get(id=id)
    art.delete()
    return redirect('main')


def change_art(request, id):

    if request.method == "POST":
        art = Articles.objects.get(pk=id)
        art.title = request.POST["title"]
        art.content = request.POST["content"]
        art.save()

    art = Articles.objects.get(pk=id)
    title = art.title
    content = art.content
    send = {"title": title,
            "content": content,
            "id": id}
    return render(request, url_names.Names.change, send)

def main_us(request, page=1):
    saved = False

    if request.method == "POST":
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Articles()
            content = MyProfileForm.cleaned_data["content"]
            title = MyProfileForm.cleaned_data["title"]

            if len(content) > 0 and len(title) > 0:
                name = request.user
                user = User.objects.get(username=name)

                profile.content = content
                profile.title = title
                profile.img = MyProfileForm.cleaned_data["picture"]
                profile.user = user
                profile.save()
                saved = True


    all = Articles.objects.all().values_list()
    paginator = Paginator(all, 5)
    context = {'articles': paginator.page(page),
               'saved': saved}

    return render(request, url_names.Names.main, context)
