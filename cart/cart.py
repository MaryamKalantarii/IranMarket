
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

    def clear(self):
        """پاک کردن کامل سبد خرید"""
        self._cart = self.session["cart"] = {"items": []}
        self.save()

    def get_cart_dict(self):
        """دریافت دیکشنری سبد خرید"""
        return self._cart
    
    def get_cart_items(self):
        """دریافت آیتم‌های سبد خرید همراه با اطلاعات مدل و قیمت کل"""
        for item in self._cart["items"]:
            model_name = item.get("model_name")  # دریافت نام مدل برای هر آیتم
            if model_name:
                # واکشی مدل بر اساس نام
                model_class = globals().get(model_name)
                if model_class:
                    # واکشی محصول از مدل مشخص
                    product_obj = model_class.objects.get(id=item["product_id"], status=True)
                    # محاسبه قیمت کل برای آیتم
                    item.update({
                        "product_obj": product_obj,
                        "total_price": item["quantity"] * product_obj.get_price()
                    })
                else:
                    raise ValueError(f"Model {model_name} not found")
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