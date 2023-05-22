from django.contrib import admin
from books_market.models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Book_Category)