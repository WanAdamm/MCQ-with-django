from django.db import models

class Subjects(models.Model):
    subject = models.CharField(max_length=16)

    def __str__(self) -> str:
        return f'{self.subject}'

    class Meta:
        verbose_name_plural = 'Subject'

class Questions(models.Model):
    question = models.TextField(default='')
    option_1 = models.CharField(max_length=1024, default='')
    option_2 = models.CharField(max_length=1024, default='')
    option_3 = models.CharField(max_length=1024, default='')
    option_4 = models.CharField(max_length=1024, default='')
    answer = models.IntegerField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.question}'
    
    class Meta:
        verbose_name_plural = 'Question'