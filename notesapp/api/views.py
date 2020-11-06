from rest_framework import status
from rest_framework.response import Response
from notesapp.models import Note
from notesapp.api.serializer import NoteSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def create_note(request):
    data = {}
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save()
            data['author'] = request.user.pk
            data['title'] = note.title
            data['description'] = note.description
            data['date_created'] = note.date_created
            data['date_published'] = note.date_published
            data['pk'] = note.pk
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewNote(RetrieveAPIView):
    queryset = Note.objects.all().order_by('date_created').select_related('author')
    serializer_class = NoteSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AllNotes(ListAPIView):
    queryset = Note.objects.all().order_by('date_created').select_related('author')
    serializer_class = NoteSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'author__username')


class AllPublishedNotes(ListAPIView):
    queryset = Note.objects.filter(is_published=True).order_by('date_created').select_related('author')
    serializer_class = NoteSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = [AllowAny, ]
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'author__display_name')


class AllUnPublishedNotes(ListAPIView):
    queryset = Note.objects.filter(is_published=False).order_by('date_created').select_related('author')
    serializer_class = NoteSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'author__display_name')


@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def publish_note(request, pk):
    data = {}
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if note.author == request.user:
        if request.method == 'PUT':
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                note = serializer.save()
                data['response'] = 'Successfully published note'
                data['title'] = note.title
                data['description'] = note.description
                data['author'] = request.user.pk
                data['date_created'] = note.date_created
                data['date_published'] = True
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    else:
        data['response'] = 'You do not have permission to publish this'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def delete_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if note.author == request.user:
        if request.method == 'DELETE':
            data = {}
            note_deleted = note.delete()
            if note_deleted:
                data['response'] = 'Note deleted successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def my_published_notes(request):
    if request.method == 'GET':
        notes = Note.objects.filter(is_published=True, author=request.user.pk).order_by('date_created').\
            select_related('author')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def my_unpublished_notes(request):
    if request.method == 'GET':
        notes = Note.objects.filter(is_published=False, author=request.user.pk).order_by('date_created').\
            select_related('author')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)