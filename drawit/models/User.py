from django.db import models

class User(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
