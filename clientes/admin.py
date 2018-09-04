from django.contrib import admin
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary','photo')
        })
    )

    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'photo')
    list_filter = ('age', 'salary')

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__age', 'desconto', 'numero')
    list_display = ('id', 'pessoa', 'desconto', 'valor', 'impostos', 'get_total')

    def get_total(self, object):
        return object.get_total()

        get_total.short_description = 'Total'


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)


