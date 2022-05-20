from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api_rest.serializers import PostSerializer, CommentariesSerializer
from core.models import Post, Commentaries


class ReceiptsViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        GenericViewSet
    ):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

    def get_queryset(self):
        queryset = Post.objects.all()
        cat = self.request.query_params.get('cat')
        if cat is not None:
            queryset = queryset.filter(cat__category=cat)
        return queryset

    @action(methods=['GET'], detail=False)
    def fast_to_cook(self, request, *args, **kwargs):
        qs = Post.objects.filter(Q(time_to_cook__lte=20) | Q(cat__category__iexact="быстрое приготовление"))
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class CommentariesViewSet(ModelViewSet):
    queryset = Commentaries.objects.all()
    serializer_class = CommentariesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'comment']