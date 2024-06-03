from rest_framework import pagination

class CustomePaginate(pagination.PageNumberPagination):
    page_size = 1