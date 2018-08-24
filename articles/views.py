import url_names
from Libraries import *
from articles.models import Articles


def create_art(request):
    if request.method == "POST":
        content = request.POST["content"]
        title = request.POST["title"]
        name = request.user.name
        user = User.objects.get(username=name)

        Articles.objects.create(content=content, title=title, user_id=user)

        return render(request, 'main')
    else:
        return render(request, 'main')


def delete_art(request, id):
    art = Articles.objects.get(pk=id)
    art.delete()
    return render(request, 'main')


def main_us(request, page=1):
    all = Articles.objects.all()
    paginator = Paginator(all, 5)
    context = {'articles': paginator.page(page)}

    return render(request, url_names.Names.main, context)
