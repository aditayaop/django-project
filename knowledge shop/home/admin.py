from django.contrib import admin

from home.models import Contact, Book, Fibuy, Sell

# Register your models here.
# class HomeAdmin(admin.ModelAdmin):
# list_display = ('name', 'email')

admin.site.register(Contact)
admin.site.register(Book)
admin.site.register(Fibuy)
admin.site.register(Sell)
