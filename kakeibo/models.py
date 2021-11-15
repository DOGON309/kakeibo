from django.db import models

class seikyumodel(models.Model):
    uuid = models.UUIDField()
    to = models.CharField(max_length=100)
    jpy = models.IntegerField()
    date = models.DateField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.to
    
    class Meta:
        verbose_name = '経費'
        verbose_name_plural = '経費'
        ordering = ('-date',)