from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Product, Comment
from .forms import AddCommentForm
from cart.forms import AddToCartProductForm


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(active=True)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.active_comment_manage.all()
        context['add_to_cart_form'] = AddToCartProductForm()
        context['comment_form'] = AddCommentForm

        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = AddCommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.product = get_object_or_404(Product, id=int(self.kwargs['product_id']))
        return super().form_valid(form)

