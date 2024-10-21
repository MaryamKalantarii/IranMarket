from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import redirect
from django.urls import reverse_lazy
class DashboardHomeView(View,LoginRequiredMixin):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # if request.user.is_authenticated:
        #     if request.user.type ==

        # else:
        #     redirect(reverse_lazy('accounts:login'))
        return super().dispatch(request, *args, **kwargs)
