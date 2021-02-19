from django.db import models

CONTAMINANT_AREA = [
    ('', 'Choose Area'),
    ('Outdoors', 'Outdoors'),
    ('Kitchen', 'Kitchen'),
    ('Living Room', 'Living Room'),
    ('Bedroom', 'Bedroom'),
    ('Bathroom', 'Bathroom')
]


class Data(models.Model):
    contaminant_area = models.CharField(choices=CONTAMINANT_AREA, max_length=40)
    image = models.ImageField(upload_to='image/data')
    tag = models.CharField(max_length=50, help_text='Add a tag')
    description = models.TextField(max_length=250, help_text='Add a description')

    def __str__(self):
        return self.contaminant_area


class Dataset(models.Model):
    title = models.CharField(max_length=200, help_text='Add a title to dataset')
    contaminant_levels = models.CharField(max_length=30, help_text='Add a contaminant level')
    health_status = models.CharField(max_length=80, help_text='Add health Status')

    def __str__(self):
        return self
