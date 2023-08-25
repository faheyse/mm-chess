from django.contrib import admin

from .models import School, Signup, Term, Product, Price


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(School)
admin.site.register(Signup)
admin.site.register(Term)

admin.site.register(Product, ProductAdmin)
admin.site.register(Price)