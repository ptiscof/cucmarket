from django.http import HttpRequest, HttpResponse
from books_market.serializer import *
from rest_framework.pagination import PageNumberPagination

# Create your views here.
from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    class Pagination(PageNumberPagination):
        # 默认页面大小
        page_size = 5
        # 页面大小对应的查询参数
        page_size_query_param = 'size'
        # 页面大小的最大值
        max_page_size = 5

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination



