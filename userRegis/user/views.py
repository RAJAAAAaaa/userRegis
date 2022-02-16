from django.shortcuts import render
from django.http import HttpResponse
from .serializers import HistoryListingSerializer
from .models import *

response = HttpResponse()


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def history_user(self, request):
        serializer_class = HistoryListingSerializer
        queryset = Poll.history.filter(history_user=request.user)
        data = self.serializer_class(queryset, many=True).data
        return response(data)

