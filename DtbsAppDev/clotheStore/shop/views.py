from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    print(category_slug)
    return render(request, 'shop/product/product_list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/product_page.html',
                  {'product': product, 'cart_product_form': cart_product_form})


class AddProductView(CreateView):
    model = Product
    # form_class = ProductForm
    template_name = 'shop/crud/create.html'
    fields = '__all__'


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'shop/crud/update.html'
    fields = '__all__'


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'shop/crud/delete.html'
    success_url = reverse_lazy('shop:product_list')
