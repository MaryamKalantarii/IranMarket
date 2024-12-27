from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import WishlistProductModel

class WishlistAdminForm(forms.ModelForm):
    product_selector = forms.ChoiceField(label="Product")  # فیلد سفارشی برای نمایش محصولات

    class Meta:
        model = WishlistProductModel
        fields = ['user', 'product_selector']  # استفاده از فیلد ترکیب‌شده

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        product_choices = []
        content_types = ContentType.objects.filter(
            model__in=['clothing', 'dijitalgoods', 'homeappliances', 'beauty', 'appliances', 'supermarket', 'child_and_baby']
        )  # مدل‌های موردنظر
        for ct in content_types:
            model_class = ct.model_class()
            if model_class:
                for product in model_class.objects.all():
                    product_choices.append((f"{ct.pk}-{product.pk}", f"{product.title} ({ct.model})"))

        self.fields['product_selector'].choices = product_choices

    def save(self, commit=True):
        instance = super().save(commit=False)

        # مقداردهی فیلدهای مرتبط با محصول
        if 'product_selector' in self.cleaned_data:
            product_data = self.cleaned_data['product_selector'].split('-')
            content_type_id, object_id = int(product_data[0]), int(product_data[1])
            instance.content_type_id = content_type_id
            instance.object_id = object_id

        if commit:
            instance.save()
        return instance

