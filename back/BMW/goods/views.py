from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from goods.models import Categories, Goods


# Create your views here.

# class Catalog(ListView):
#     pass

def catalog(request):
    categorie = Categories.objects.all()

    context = {
        'categories': categorie,
    }
    return render(request, 'goods/catalog.html', context)


# def categories(request):
#     return render(request, 'goods/categories.html')

class CategoriesView(ListView):
    model = Goods
    template_name = "goods/categories.html"
    context_object_name = 'goods'
    allow_empty = False

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')

        if category_slug == "all":
            goodies = super().get_queryset()
        else:
            goodies = super().get_queryset().filter(category__slug=category_slug)
        return goodies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


class GoodsView(DetailView):
    template_name = "goods/goods.html"
    slug_url_kwarg = 'goods_slug'
    context_object_name = 'good'

    def get_object(self, queryset=None):
        good = Goods.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return good

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


# def goods(request):
#     context = {
#         'goods': Goods.objects.all()
#     }
#     return render(request, 'goods/goods.html', context)
