from django.db import models

#  models


from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the KFC ordering system.
    """
    full_name = models.CharField(max_length=200, help_text="Full name of the customer")
    email_address = models.EmailField(unique=True, help_text="Unique email address of the customer")

    def __str__(self):
        return self.full_name


class Order(models.Model):
    """
    Represents an order placed by a customer for KFC.
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="Customer who placed the order"
    )
    placed_at = models.DateTimeField(auto_now_add=True, help_text="Date and time the order was placed")
    amount_due = models.DecimalField(max_digits=12, decimal_places=2, help_text="Total amount to be paid for the order")
    order_details = models.TextField(help_text="Details of the KFC items ordered")

    def __str__(self):
        return f"Order {self.id} - {self.customer.full_name}"

