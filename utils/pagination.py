from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)
from rest_framework.response import Response
from .response import CustomResponse


class CustomPageNumberPagination(PageNumberPagination):
    """重写PageNumberPagination, 自定义字段名称"""

    page_size = 10  # 设置默认每页返回数据量
    page_size_query_param = "size"  # 自定义page_size在链接中的参数名称
    max_page_size = 50  # 设置每页最大数据返回量


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 50


class CustomCursorPagination(CursorPagination):
    page_size = 10
    page_size_query_param = "page_size"
    cursor_query_param = "cursor"
    ordering = "id"  # 默认采用“created”进行排序，故自定义排序字段
