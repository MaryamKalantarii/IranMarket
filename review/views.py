from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import ReviewModel

class SubmitReviewView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        model_name = request.POST.get("model_name")
        description = request.POST.get("description")
        

        # بررسی مقادیر ارسال شده از فرم
        if not product_id or not model_name or not description:
            messages.error(request, "فیلد توضیحات اجباری است")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            # پیدا کردن مدل مرتبط با محصول
            content_type = ContentType.objects.get(model=model_name)
            product = content_type.get_object_for_this_type(pk=product_id)

            # ذخیره نظر در مدل ReviewModel
            review = ReviewModel.objects.create(
                user=request.user,
                product=product,
                description=description,
            )
            review.save()

            messages.success(request, "نظر شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        except ContentType.DoesNotExist:
            messages.error(request, "مدل محصول یافت نشد.")
            return redirect(request.META.get("HTTP_REFERER", "/"))
        except Exception as e:
            messages.error(request, f"خطایی رخ داد: {str(e)}")
            return redirect(request.META.get("HTTP_REFERER", "/"))

            
       