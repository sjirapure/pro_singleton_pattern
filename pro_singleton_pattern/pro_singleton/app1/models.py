from django.db import models

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    
    
    
class Employee(SingletonModel):
    eid = models.IntegerField()
    name = models.CharField(max_length=50)
    sal = models.FloatField()
    city = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.eid}--{self.name}'
        