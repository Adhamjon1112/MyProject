from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Note


User = get_user_model()

admin.site.register(User)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created', 'updated')
    list_filter = ('owner', 'created', 'updated')
    search_fields = ('title', 'description')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'owner')
        }),
        ('Date Information', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

    class Media:
        css = {
            'all': ('notes/admin.css',)
        }