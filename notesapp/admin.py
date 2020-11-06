from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_created', 'title', 'author', 'is_published', )


admin.site.register(Note, NoteAdmin)