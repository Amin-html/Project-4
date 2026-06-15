from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from games.models import Game

@login_required
def cart_add(request, product_pk):
    product = get_object_or_404(Game, pk=product_pk)

    # Исправлено: 'product=' заменено на 'game='
    # Добавлено: defaults={'quantity': 1} для корректной инициализации новой записи
    item, created = CartItem.objects.get_or_create(
        user=request.user,
        game=product,
        defaults={'quantity': 1}
    )

    # Если товар уже был в корзине, увеличиваем количество
    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')


@login_required
def cart_detail(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total': total,
    })

@login_required
def cart_remove(request, item_pk):
    item = get_object_or_404(CartItem, pk=item_pk, user=request.user)
    item.delete()
    return redirect('cart_detail')

# Create your views here.
