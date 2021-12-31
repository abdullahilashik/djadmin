from django.db import models
from django.utils.text import slugify

class JobCategory(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)    


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super(JobCategory, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Job Categories'

class Location(models.Model):
    title = models.CharField(max_length=250)


class Job(models.Model):

    JOB_LOCATION_CHOICES = (
        ('dhaka','Dhaka'),
        ('rajshahi','Rajshahi'),
        ('chittagong',"Chittagong"),
        ('khulna','Khulna'),
        ('sylhet','Sylhet'),
        ('all','All Bangladesh')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    job_category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    min_salary = models.FloatField(default=0.0)
    max_salary = models.FloatField(default=0.0)
    location = models.ManyToManyField(Location)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'All Jobs'