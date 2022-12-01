from django.views.generic import DetailView

from .models import Product


class ProductDetailView(DetailView):
    """
    View to details of the selected product
    """
    template_name = "product/product_detail.html"
    model = Product
