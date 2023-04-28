from django.contrib import admin
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    # Declare Full name
    def full_name(self, obj):
        # All the operation
        print(obj)
        return obj.first_name + ' ' + obj.last_name
    # Search
    search_fields = ('first_name',)
    # Filter
    list_filter = ('job', 'habilidades', 'departamento')
    # Horizontal filter for adding
    filter_horizontal = ('habilidades',)

# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)   
admin.site.register(Habilidades)

