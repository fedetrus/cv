from django.contrib import admin
from .models import Technology, Project, ProjectImage

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name','nro_orden', 'status')
    search_fields = ('name','nro_orden', 'status')

    def get_changeform_initial_data(self, request):
        """ Prellena el campo nro_orden con el siguiente número disponible """
        last_order = Technology.objects.order_by('-nro_orden').first()
        next_order = (last_order.nro_orden + 1) if last_order else 1
        return {'nro_orden': next_order}
    
class ProjectImageInline(admin.TabularInline):  # O usa StackedInline si prefieres
    model = ProjectImage
    extra = 1  # Muestra un campo extra vacío para agregar más imágenes
    fields = ['image']  # Solo muestra el campo de la imagen en el inline

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'nro_orden', 'description', 'status', 'inicio')
    search_fields = ('title', 'nro_orden', 'description', 'status', 'inicio')
    inlines = [ProjectImageInline]  # Agrega el inline de imágenes en el admin

    def get_changeform_initial_data(self, request):
        """ Prellena el campo nro_orden con el siguiente número disponible """
        last_order = Project.objects.order_by('-nro_orden').first()
        next_order = (last_order.nro_orden + 1) if last_order else 1
        return {'nro_orden': next_order}