from django.db import models
from django.utils.translation import gettext_lazy as _

from django.urls import reverse
from core.model_mixins import DiscountMixin


class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=100)
    description = models.TextField(_("Product Description"), blank=True)
    unit_in_stock = models.IntegerField(_("Units in Stock"), default=0)
    reward_points_credit = models.IntegerField(
        _("Reward Points Credit"), default=0)
    # category = models.ForeignKey("Category", verbose_name=_("Category"))
    discount = models.ForeignKey(
        "Discount",
        verbose_name=_("Discount"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="products",
    )

    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Pricing(models.Model):
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="pricing",
    )
    base_price = models.DecimalField(
        _("Base Price"), max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_expired = models.DateTimeField(
        _("Date Expired"), blank=True, null=True)

    in_active = models.BooleanField(_("In Active"), default=True)

    def __str__(self):
        return f"{self.product.name} - {self.base_price}"


class Discount(DiscountMixin, models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="discounts"
    )

    def __str__(self):
        return f"{self.product.name} - {self.discount_value} - {self.discount_unit}"
