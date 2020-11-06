from rest_framework import serializers
from notesapp.models import Note


class NoteSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField('get_display_name')

    class Meta:
        model = Note
        fields = ('pk', 'date_created', 'date_published', 'title', 'description', 'is_published', 'display_name', )

    def get_display_name(self, request):
        name = request.author.display_name
        return name