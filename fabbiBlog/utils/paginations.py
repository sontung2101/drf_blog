import math

from django.core.paginator import InvalidPage
from rest_framework import pagination
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from collections import OrderedDict
from utils.error import PageNotFound


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 4
    max_limit = 10

    def get_paginated_response(self, data):
        total_page = math.ceil(self.count / self.limit)
        return Response({
            'links': {
                'prev': self.get_previous_link(),
                'next': self.get_next_link(),
                'count': int(self.count),
                'total_pages': total_page,
            },
            'data': data
        })


class CustomPagination2(pagination.PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'previous': self.get_previous_link(),
                'next': self.get_next_link(),
                'count': self.page.paginator.count,
                'currentPage':self.page.number,
                'total_page':self.page.paginator.num_pages,
            },
            'data': data
        })

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise PageNotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)
class CustomPagination3(CustomPagination2):
    page_size = 3