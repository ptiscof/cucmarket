from django.contrib import admin
from books_market.models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(BooksCategory)
admin.site.register(OrderInfo)
admin.site.register(OrderBooks)