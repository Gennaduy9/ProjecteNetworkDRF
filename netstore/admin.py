from django.contrib import admin

from netstore.models import Product, Contact, Seller

# Регистрируем модели Product и Contact в административной панели
admin.site.register(Product)
admin.site.register(Contact)


# Функция действия для обновления задолженности
@admin.action(description='Списание задолженности')
def make_published(modeladmin, request, queryset):
    queryset.update(debt=0)


# Регистрируем модель Seller и настраиваем ее административное представление
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller_type', 'supplier',)
    list_filter = ('seller_type', 'contact__city',)
    actions = [make_published]  # Добавляем действие "Списание задолженности"

    def contact_city(self, obj):
        return obj.contacts.city
