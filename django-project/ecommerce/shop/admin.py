from django.contrib import admin

# Register your models here.
from .models import Product,Order

class ProductAdmin(admin.ModelAdmin):
    
    def category_to_chamge_default(self,request,queryset):
        queryset.update(category="default")
        
    category_to_chamge_default.short_description ='Default Category'  
    list_display=('title','price','discount_price','category','description',)
    search_fields= ('title',)
    actions =('category_to_chamge_default',)
    list_editable = ('description',)
    
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shoping"
admin.site.index_title ="Manage ABC Shopping"
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)



