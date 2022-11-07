from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.model_mixins import DiscountMixin


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    max_reward_points_encash = models.IntegerField(
        _("Max Reward Points Encash"), default=0)
    parent_category = models.ForeignKey(
        "self",
        verbose_name=_("Parent Category"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    # parent_category = models.ForeignKey(
    #     "Product.category",
    #     verbose_name=_("Parent Category"),
    #     blank=True,
    #     null=True,
    #     on_delete=models.CASCADE,
    # )


class Discount(DiscountMixin, models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.discount_value} - {self.discount_unit}"
