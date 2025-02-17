from django.contrib import admin
from .models import Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')  # Muestra el nombre y una vista previa del logo
    search_fields = ('name',)  # Permite buscar por nombre
    readonly_fields = ('logo_preview',)  # La vista previa solo para visualización

    def logo_preview(self, obj):
        """Muestra una vista previa de la imagen en el panel de administración"""
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="50" height="50" style="border-radius:5px;"/>'
        return "(No image)"
    
    logo_preview.allow_tags = True
    logo_preview.short_description = "Preview"

