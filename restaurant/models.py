from django.db import models
from django.utils import timezone


class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    status = models.CharField(max_length=20,choices=[('free','free'),('occupied','occupied')])


    def __str__(self):
        return f"Table {self.number} - ({self.seats} Seats)"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    available = models.CharField(max_length=100,choices=[('Yes','Yes'), ('No','No')])
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)


    def __str__(self):
        return self.name



class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=100,choices=[("Pending", "Pending"), ("served", "served")])
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Order {self.id} - Table {self.table.number} - {self.status}"

    @property
    def total(self):
        order_items = self.order_items.all()
        if order_items.exists():
            return sum(oi.item.price * oi.quantity for oi in order_items)
        return sum(item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} x{self.quantity}"