from django.contrib import admin
from .models import Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name','nro_orden', 'status')
    search_fields = ('name','nro_orden', 'status')

    def get_changeform_initial_data(self, request):
        """ Prellena el campo nro_orden con el siguiente número disponible """
        last_order = Technology.objects.order_by('-nro_orden').first()
        next_order = (last_order.nro_orden + 1) if last_order else 1
        return {'nro_orden': next_order}