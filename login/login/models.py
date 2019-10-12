from django.db import models

class Upload(models.Model):

    arquivo = models.FileField(upload_to='files/')