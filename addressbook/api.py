from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from contacts.models import Contact

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
	allowed_methods = ['get']	

class RecipeResource(ModelResource):
    conatct = fields.ForeignKey(UserResource, 'Contact')

class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()
        resource_name = 'contact'
	authorization = Authorization()
	allowed_methods = ['get']
