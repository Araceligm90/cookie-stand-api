from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookie-stand/cookie_stand_list.html"
    model = CookieStand
    context_object_name = "cookie-stand"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie-stand/cookie_stand_detail.html"
    model = CookieStand


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie-stand/cookie_stand_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie-stand/cookie_stand_create.html"
    model = CookieStand
    fields = [
        "location",
        "minimum_customers_per_hour",
        "maximum_customers_per_hour",
        "description",
        "owner",
        "average_cookies_per_sale"
    ]
    # fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie-stand/cookie_stand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_stand_list")
