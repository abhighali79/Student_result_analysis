from django.db import models
from users.models import Branch,Batch,CustomUser

class Document(models.Model):
    usn=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    sem=models.IntegerField()
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.file.name

class marks(models.Model):
    # file=models.ForeignKey(Document, on_delete=models.CASCADE)
    usn = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sem = models.IntegerField()
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    internal = models.CharField(max_length=10)
    external = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usn

