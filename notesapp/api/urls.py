from django.urls import path
from notesapp.api.views import AllNotes, AllUnPublishedNotes, publish_note, delete_note, AllPublishedNotes, ViewNote, \
    my_unpublished_notes, my_published_notes, create_note
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'notesapp'

urlpatterns = [
    path('view/<int:pk>/', ViewNote.as_view(), name='viewNote'),
    path('create/', create_note, name='createNote'),
    path('list/', AllNotes.as_view(), name='list'),
    path('published_notes/', AllPublishedNotes.as_view(), name='all_published_notes'),
    path('unpublished_notes/', AllUnPublishedNotes.as_view(), name='unpublished_notes'),
    path('my_published_notes/', my_published_notes, name='my_p_notes'),
    path('my_unpublished_notes/', my_unpublished_notes, name='my_unp_notes'),
    path('publish/<int:pk>/', publish_note, name='publish_note'),
    path('delete/<int:pk>/', delete_note, name='delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)