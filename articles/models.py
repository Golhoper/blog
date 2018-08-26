from Libraries import *
from django.db import models


class Articles(models.Model):

    class Meta:
        db_table = "articles"
        verbose_name = "article"
        verbose_name_plural = "article_pl"
        required_db_vendor = "mysql"

    id = models.AutoField(primary_key=True)
    content = models.TextField(blank=False, null=False, default="Nothing here")
    title = models.TextField(blank=False, null=False, default="Default title")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, help_text="creation time")
    img = models.ImageField(upload_to="articles/")