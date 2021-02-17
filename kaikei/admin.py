from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Customer, Hoken, Jiseki, Buturyou, Shouhin, Product, Payment, Staff, Choice

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    list_display = ['username', 'email', 'age']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Hoken)
admin.site.register(Jiseki)
admin.site.register(Buturyou)
admin.site.register(Shouhin)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Staff)
admin.site.register(Choice)