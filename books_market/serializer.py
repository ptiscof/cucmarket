from books_market.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    #覆盖外键字段
    class Meta:
        model = Book
        fields = '__all__'

class BookCategorySerializer(serializers.ModelSerializer):
    #覆盖外键字段
    class Meta:
        model = Book_Category
