from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import CartItemModel

class CartItemAdminForm(forms.ModelForm):
    product_selector = forms.ChoiceField(label="Product")  # فیلد سفارشی برای نمایش محصولات

    class Meta:
        model = CartItemModel
        fields = ['cart', 'quantity', 'product_selector']  # استفاده از فیلد ترکیب‌شده

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        product_choices = []
        content_types = ContentType.objects.filter(model__in=['clothing', 'dijitalgoods','homeappliances','beauty','appliances','supermarket','child_and_baby'])  # مدل‌های موردنظر
        for ct in content_types:
            model_class = ct.model_class()
            if model_class:
                for product in model_class.objects.all():
                    product_choices.append((f"{ct.pk}-{product.pk}", f"{product.title} ({ct.model})"))

        self.fields['product_selector'].choices = product_choices

    def save(self, commit=True):
        instance = super().save(commit=False)

        # اطمینان از اینکه محصول انتخاب شده
        if 'product_selector' in self.cleaned_data:
            product_data = self.cleaned_data['product_selector'].split('-')
            instance.product_content_type_id = product_data[0]  # شناسه ContentType
            instance.product_object_id = product_data[1]        # شناسه محصول

        if commit:
            instance.save()
        return instance
