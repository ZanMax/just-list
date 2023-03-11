from django.shortcuts import render
from django.views import View
from .models import Category, Item


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "idioms/index.html", {"categories": categories})


class ItemView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, "idioms/index.html", {"items": items})


class IndexView(View):
    def get(self, request):
        return render(request, "main/index.html")
