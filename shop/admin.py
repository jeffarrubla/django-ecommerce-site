from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):	
	list_display = ('title','price','discount_price','category','description','image')
	search_fields = ('category',)
	actions = ('change_category_to_default',) 

	def change_category_to_default(self, request, queryset):
		queryset.update(category='default')

	change_category_to_default.short_description = 'Default Category'

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
