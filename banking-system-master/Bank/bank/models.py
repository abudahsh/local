from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
	name= models.CharField(max_length=50)
	dob= models.DateField()
	phone= models.PositiveIntegerField()
	address= models.TextField()
	email= models.EmailField()
	accnum= models.PositiveIntegerField()
	created= models.DateTimeField(auto_now_add=True)
	amount= models.FloatField() 
	def __unicode__(self):
		return self.name

class PersonAdmin(admin.ModelAdmin):
	list_display=('name','email','amount')
	search_fields =('accum',)
	
	
admin.site.register(Person,PersonAdmin)

