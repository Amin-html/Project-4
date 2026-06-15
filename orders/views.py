from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction # 🛠️ Импортируем модуль транзакций
from .models import Order, OrderItem
from cart.models import CartItem

@login_required
def order_create(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items:
        return redirect('cart_detail')

    if request.method == 'POST':
        total = sum(item.total_price() for item in cart_items)

        # 🛠️ ИСПРАВЛЕНО: Заворачиваем в транзакцию для безопасности данных
        with transaction.atomic():
            # создаём заказ
            order = Order.objects.create(
                user=request.user,
                total_price=total
            )

            # создаём позиции заказа
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    game=item.game, # Передаем правильное поле game
                    quantity=item.quantity,
                    price=item.game.price
                )

            # очищаем корзину только после успешного создания всех OrderItem
            cart_items.delete()

        return redirect('order_detail', pk=order.pk)

    total = sum(item.total_price() for item in cart_items)
    return render(request, 'orders/order_create.html', {
        'cart_items': cart_items,
        'total': total,
    })

@login_required
def my_orders(request):
    # Сортировку лучше сделать по убыванию '-created_at', чтобы новые заказы были сверху
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
