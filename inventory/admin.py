from django.contrib import admin
from django.contrib.auth.models import Group, User

from inventory.models import Project, Element

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'visible', 'display_list_image',)
    readonly_fields = ('display_image', 'display_list_image', 'created_at', 'updated_at')
    list_per_page = 10
    ordering = ('name',)


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_project', 'created_at', 'updated_at', 'visible', 'display_list_image',)
    readonly_fields = ('display_image', 'display_list_image', 'created_at', 'updated_at')
    ordering = ('name', 'parent_project')
    list_per_page = 10

    list_filter = ('parent_project',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_project":
            kwargs["queryset"] = Project.objects.filter(visible=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
