from django.apps import AppConfig


class PpmProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ppm_products"

    def ready(self):
        import ppm_products.signals
