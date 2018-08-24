from Libraries import *


class SecretWords(models.Model):
    class Meta:
        db_table = "secretwords"
        verbose_name = "secret_words"
        verbose_name_plural = "secret_words_pl"
        required_db_vendor = "mysql"

    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100, blank=False, null=False, default="no word")
