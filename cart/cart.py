from django.apps import apps
from .models import CartItemModel,CartModel
from django.contrib.contenttypes.models import ContentType

class CartSession():
    def __init__(self, session):
        self.session = session
        # اگر سبد خرید وجود نداشت، یک سبد خرید جدید ایجاد می‌کند
        self._cart = self.session.setdefault("cart", {"items": []})
        
    def add_product(self, product_id, model_name):
        """افزودن محصول به سبد خرید"""
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                # اگر محصول قبلاً وجود دارد، فقط تعداد را افزایش می‌دهد
                item["quantity"] += 1
                break
        else:
            # ایجاد آیتم جدید برای سبد خرید
            new_item = {
                "product_id": product_id,
                "quantity": 1,
                "model_name": model_name  # اضافه کردن model_name به آیتم
            }
            self._cart["items"].append(new_item)
        
        self.save()  # ذخیره سشن بعد از هر تغییر

    def update_product_quantity(self,product_id,quantity):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] = int(quantity)
                break
        else:
            return
        self.save()

    def remove_product(self,product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                self._cart["items"].remove(item)
                break
        else:
            return
        self.save()

    def clear(self):
        """پاک کردن کامل سبد خرید"""
        self._cart = self.session["cart"] = {"items": []}
        self.save()

    def get_cart_dict(self):
        return self._cart

    def get_cart_items(self):
        """دریافت آیتم‌های سبد خرید همراه با اطلاعات مدل و قیمت کل"""
        for item in self._cart["items"]:
            model_name = item.get("model_name")  # دریافت نام مدل برای هر آیتم
            if model_name:
                try:
                    # واکشی مدل از اپلیکیشن product و نام مدل
                    model_class = apps.get_model('product', model_name)
                    
                    # واکشی محصول از مدل مشخص
                    product_obj = model_class.objects.get(id=item["product_id"], status=True)
                    
                    # محاسبه قیمت کل برای آیتم
                    item.update({
                        "product_obj": product_obj,
                        "total_price": item["quantity"] * product_obj.get_price()
                    })
                except LookupError:
                    raise ValueError(f"Model {model_name} not found in app 'product'")
                except model_class.DoesNotExist:
                    raise ValueError(f"Product with ID {item['product_id']} not found in model {model_name}")
            else:
                raise ValueError("Model name not specified in cart item")
        
        return self._cart["items"]

    def get_total_payment_amount(self):
        """محاسبه مبلغ کل سبد خرید"""
        return sum(item["total_price"] for item in self._cart["items"])

    def get_total_quantity(self):
        """محاسبه تعداد کل آیتم‌های سبد خرید"""
        return sum(item["quantity"] for item in self._cart["items"])

    def save(self):
        """ذخیره تغییرات سبد خرید در session"""
        self.session.modified = True

    def sync_cart_items_from_db(self, user):
        """همگام‌سازی اقلام سبد خرید در سشن با دیتابیس هنگام ورود کاربر"""
        if not user.is_authenticated:
            return

        cart, _ = CartModel.objects.get_or_create(user=user)
        
        # بررسی وضعیت سشن قبل از همگام‌سازی
        print(f"Session before sync: {self._cart['items']}")

        db_items = CartItemModel.objects.filter(cart=cart)
        for db_item in db_items:
            product_id = db_item.product_object_id
            model_name = db_item.product_content_type.model
            quantity = db_item.quantity

            # بررسی وجود محصول در سشن
            for session_item in self._cart["items"]:
                if session_item["product_id"] == str(product_id) and session_item["model_name"] == model_name:
                    session_item["quantity"] = quantity
                    break
            else:
                self._cart["items"].append({
                    "product_id": str(product_id),
                    "quantity": quantity,
                    "model_name": model_name
                })

        # بررسی وضعیت سشن بعد از همگام‌سازی
        print(f"Session after sync: {self._cart['items']}")
        self.merge_session_cart_in_db(user)


    def merge_session_cart_in_db(self, user):
        """انتقال اقلام سبد خرید سشن به دیتابیس هنگام خروج کاربر"""
        if not user.is_authenticated:
            return  # اگر کاربر وارد نشده باشد، کاری انجام نمی‌شود

        # گرفتن یا ساختن سبد خرید مرتبط با کاربر
        cart, _ = CartModel.objects.get_or_create(user=user)

        # بررسی وضعیت سشن قبل از انتقال به دیتابیس
        print(f"Session before merge: {self._cart['items']}")

        # --- 1. انتقال اقلام سشن به دیتابیس ---
        for session_item in self._cart["items"]:
            model_name = session_item["model_name"]
            product_id = int(session_item["product_id"])
            quantity = session_item["quantity"]

            try:
                # واکشی ContentType و محصول
                content_type = ContentType.objects.get(model=model_name)
                product_obj = content_type.get_object_for_this_type(id=product_id)
            except ContentType.DoesNotExist:
                continue  # اگر مدل پیدا نشد، رد شود
            except product_obj.DoesNotExist:
                continue  # اگر محصول پیدا نشد، رد شود

            # ایجاد یا بروزرسانی آیتم در دیتابیس
            cart_item, _ = CartItemModel.objects.get_or_create(
                cart=cart,
                product_content_type=content_type,
                product_object_id=product_id
            )
            cart_item.quantity = quantity
            cart_item.save()

        # بررسی وضعیت سشن بعد از انتقال به دیتابیس
        print(f"Session after merge: {self._cart['items']}")

        # --- 2. حذف اقلام اضافی از دیتابیس ---
        session_product_ids = [
            (item["model_name"], int(item["product_id"])) for item in self._cart["items"]
        ]
        CartItemModel.objects.filter(cart=cart).exclude(
            product_content_type__model__in=[item[0] for item in session_product_ids],
            product_object_id__in=[item[1] for item in session_product_ids],
        ).delete()