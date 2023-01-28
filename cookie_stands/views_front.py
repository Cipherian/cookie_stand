from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_detail.html"
    model = CookieStand


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_create.html"
    model = CookieStand
    fields = "__all__"


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_list")
