from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import ReviewModel

class SubmitReviewForm(forms.ModelForm):
    model_name = forms.ChoiceField(
        choices=[(ct.model, ct.name) for ct in ContentType.objects.filter(app_label='shop')],
        label="نوع محصول"
    )
    product_id = forms.IntegerField(label="شناسه محصول")

    class Meta:
        model = ReviewModel
        fields = ['description', 'model_name', 'product_id']

    def clean(self):
        cleaned_data = super().clean()
        model_name = cleaned_data.get('model_name')
        product_id = cleaned_data.get('product_id')

        try:
            content_type = ContentType.objects.get(app_label='shop', model=model_name)
            product = content_type.get_object_for_this_type(id=product_id)
        except ContentType.DoesNotExist:
            raise forms.ValidationError("مدل انتخاب شده معتبر نیست.")
        except content_type.model_class().DoesNotExist:
            raise forms.ValidationError("محصول با این شناسه وجود ندارد.")

        cleaned_data['product_content_type'] = content_type
        cleaned_data['product_object_id'] = product_id
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.product_content_type = self.cleaned_data['product_content_type']
        instance.product_object_id = self.cleaned_data['product_object_id']
        if commit:
            instance.save()
        return instance

