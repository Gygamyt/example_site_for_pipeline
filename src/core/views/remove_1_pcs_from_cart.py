from django.contrib import messages
from core.models import *
from django.shortcuts import get_object_or_404, redirect


def remove_1_pcs_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        is_ordered=False,
        user=request.user
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__pk=product.pk).exists():
            item_in_order = ItemInOrder.objects.filter(
                product=product,
                user=request.user,
                is_ordered=False
            )[0]
            if item_in_order.quantity > 1:
                item_in_order.quantity -= 1
                item_in_order.save()
            else:
                order.items.remove(item_in_order)
                item_in_order.delete()
            messages.info(request, "This item quantity was updated.")
            return redirect("order_summary_url")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product_detail_url", pk=pk)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product_detail_url", pk=pk)
