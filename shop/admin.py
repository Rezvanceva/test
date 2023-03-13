from django.contrib import admin

from shop.models import Retail, Provision, Product, Contact


@admin.action()
def receivables_reset(queryset):
    queryset.update(receivables=0)


class LinkAdmin(admin.ModelAdmin):

    list_display = ('title', 'contact', 'product', 'provision', 'receivables', 'created')
    list_display_links = ('title', 'provision',)
    list_filter = ('contact__city',)
    search_fields = ('contact__city',)
    actions = (receivables_reset,)


admin.site.register(Retail, LinkAdmin)
admin.site.register(Provision)
admin.site.register(Product)
admin.site.register(Contact)
