from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'   # Allow client to set page size
    page_query_param = 'page-num'         # Rename the page query param
    max_page_size = 2                   # Maximum page size

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),       # URL for next page
            'previous': self.get_previous_link(), # URL for previous page
            'count': self.page.paginator.count,  # Total items
            'results': data                      # Paginated data
        })
