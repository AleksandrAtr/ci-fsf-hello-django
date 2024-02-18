from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, null=False,blank=False)
    done = models.BooleanField(null=False,blank=False, default=False)

    def __str__(self) -> str:
        return self.name
    
