# Generated by Django 4.1.3 on 2022-11-07 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "discount_unit",
                    models.CharField(
                        choices=[("P", "Percentage"), ("A", "Amount")],
                        max_length=1,
                        verbose_name="Discount Unit",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date Created"
                    ),
                ),
                (
                    "valid_unit",
                    models.CharField(
                        choices=[("D", "Day")], max_length=1, verbose_name="Valid Unit"
                    ),
                ),
                ("valid_value", models.IntegerField(verbose_name="Valid Value")),
                (
                    "coupon_code",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Coupon Code",
                    ),
                ),
                (
                    "discount_value",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Discount Value"
                    ),
                ),
                (
                    "minimum_order_value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Minimum Order Value",
                    ),
                ),
                (
                    "maximum_discount_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Maximum Discount Amount",
                    ),
                ),
                (
                    "is_redeem_allowed",
                    models.BooleanField(
                        default=False, verbose_name="Is Redeem Allowed"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Product Name")),
                (
                    "description",
                    models.TextField(
                        blank=True, verbose_name="Product Description"),
                ),
                (
                    "unit_in_stock",
                    models.IntegerField(
                        default=0, verbose_name="Units in Stock"),
                ),
                (
                    "reward_points_credit",
                    models.IntegerField(
                        default=0, verbose_name="Reward Points Credit"),
                ),
                ("summary", models.TextField(blank=True, null=True)),
                ("featured", models.BooleanField(default=False)),
                (
                    "discount",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.discount",
                        verbose_name="Discount",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "base_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Base Price"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date Created"
                    ),
                ),
                (
                    "date_expired",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date Expired"
                    ),
                ),
                (
                    "in_active",
                    models.BooleanField(
                        default=True, verbose_name="In Active"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pricing",
                        to="products.product",
                        verbose_name="Product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="discount",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discounts",
                to="products.product",
            ),
        ),
    ]
