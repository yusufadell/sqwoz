from django.db import models

from django.utils.translation import gettext_lazy as _

from django.core.validators import MinValueValidator, MaxValueValidator


class DiscountMixin(models.Model):
    discount_value = models.DecimalField(
        _("Discount Value"),
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    discount_unit = models.CharField(
        _("Discount Unit"), max_length=1, choices=(("P", "Percentage"), ("A", "Amount"))
    )
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    valid_unit = models.CharField(
        _("Valid Unit"), max_length=1, choices=(("D", "Day"),)
    )
    valid_value = models.IntegerField(_("Valid Value"))
    coupon_code = models.CharField(
        _("Coupon Code"), max_length=100, blank=True, null=True
    )
    discount_value = models.DecimalField(
        _("Discount Value"), max_digits=10, decimal_places=2
    )
    minimum_order_value = models.DecimalField(
        _("Minimum Order Value"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    maximum_discount_amount = models.DecimalField(
        _("Maximum Discount Amount"),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    is_redeem_allowed = models.BooleanField(_("Is Redeem Allowed"), default=False)

    class Meta:
        abstract = True


# class ProductMixin(models.Model):
#     name = models.CharField(_("Product Name"), max_length=100)
#     description = models.TextField(_("Product Description"), blank=True)
#     unit_in_stock = models.IntegerField(_("Units in Stock"), default=0)
#     reward_points_credit = models.IntegerField(_("Reward Points Credit"), default=0)
#     discount = models.ForeignKey(
#         "Discount",
#         verbose_name=_("Discount"),
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#     )

#     summary = models.TextField(blank=True, null=True)
#     featured = models.BooleanField(default=False)

#     class Meta:
#         abstract = True


# class CategoryMixin(models.Model):
#     name = models.CharField(_("Category Name"), max_length=100)
#     description = models.TextField(_("Category Description"), blank=True)
#     parent = models.ForeignKey(
#         "self",
#         verbose_name=_("Parent Category"),
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#     )

#     class Meta:
#         abstract = True
