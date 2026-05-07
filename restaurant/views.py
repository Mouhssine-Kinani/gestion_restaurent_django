from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Table, MenuItem, Order
from .forms import TableForm, MenuItemForm, OrderForm
from django.contrib.auth.decorators import login_required

# ======== Tables ========
@login_required
def table_list(request):
    query = request.GET.get('q')
    if query:
        tables = Table.objects.filter(number__icontains=query)
    else:
        tables = Table.objects.all().order_by('number')
    return render(request, 'restaurant/table_list.html', {'tables': tables})

@login_required
def add_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, 'restaurant/add_table.html', {'form': form})

@login_required
def update_table(request, id):
    table = get_object_or_404(Table, id=id)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm(instance=table)
    return render(request, 'restaurant/update_table.html', {'form': form})

@login_required
def delete_table(request, id):
    table = get_object_or_404(Table, id=id)
    if request.method == 'POST':
        table.delete()
        return redirect('table_list')
    return render(request, 'restaurant/delete_table.html', {'table': table})


# ======== Menu Items ========
@login_required
def menu_list(request):
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all().order_by('name')
    return render(request, 'restaurant/menu_list.html', {'menu_items': menu_items})

@login_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'restaurant/add_menu_item.html', {'form': form})

@login_required
def update_menu_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'restaurant/update_menu_item.html', {'form': form})

@login_required
def delete_menu_item(request, id):
    item = get_object_or_404(MenuItem, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'restaurant/delete_menu_item.html', {'item': item})


# ======== Orders ========
@login_required
def order_list(request):
    query = request.GET.get('q')
    if query:
        orders = Order.objects.filter(id__icontains=query)
    else:
        orders = Order.objects.all().order_by('-id')
    return render(request, 'restaurant/order_list.html', {'orders': orders})

@login_required
def add_order(request):
    menu_items = MenuItem.objects.all()
    tables = Table.objects.all()
    last_order = Order.objects.last()
    next_order_id = (last_order.id + 1) if last_order else 1
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'restaurant/add_order.html', {'form': form, 'menu_items': menu_items, 'tables': tables, 'next_order_id': next_order_id})

@login_required
def update_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'restaurant/update_order.html', {'form': form})

@login_required
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'restaurant/delete_order.html', {'order': order})


# ======== Authentication ========
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'restaurant/register_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('table_list')
    else:
        form = AuthenticationForm()
    return render(request, 'restaurant/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')



@login_required
def settings_view(request):
    return render(request, 'restaurant/settings.html')

@login_required
def dashboard(request):
    tables = Table.objects.all().order_by('number')
    menu_items = MenuItem.objects.all().order_by('name')
    orders = Order.objects.all().order_by('-id')

    total_revenue = sum(order.total for order in orders)
    total_orders = orders.count()
    active_tables = tables.filter(status='occupied').count()
    total_tables = tables.count()
    menu_count = menu_items.count()

    return render(request, 'restaurant/dashboard.html', {'tables': tables, 'menu_items': menu_items, 'orders': orders, 'total_revenue': total_revenue, 'total_orders': total_orders, 'active_tables': active_tables, 'total_tables': total_tables, 'menu_count': menu_count})