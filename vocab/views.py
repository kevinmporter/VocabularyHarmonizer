from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from common.models import License
from .models import Term, Relationship, TermRelationshipTerm
from .serializers import TermSerializer, RelationshipSerializer


class TermListCreateView(generics.ListCreateAPIView):
    serializer_class = TermSerializer
    queryset = Term.objects.all()


class TermDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TermSerializer
    queryset = Term.objects.all()


class RelationshipListCreateView(generics.ListCreateAPIView):
    serializer_class = RelationshipSerializer
    queryset = Relationship.objects.all()


class RelationshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RelationshipSerializer
    queryset = Relationship.objects.all()


class MainPageView(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        params = {
            'terms': Term.objects.all(),
            'relationships': Relationship.objects.all(),
            'licenses': License.objects.all(),
        }
        return Response(params, template_name='vocab/main_page.html',
                        status=status.HTTP_200_OK)


class VocabGraphView(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        params = {
            'terms': Term.objects.all(),
            'relationships': Relationship.objects.all(),
        }
        return Response(params, template_name='vocab/vocab_graph.html',
                        status=status.HTTP_200_OK)


class EditTermView(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        term_id = request.query_params.get('id')
        term = Term.objects.get(id=term_id)
        params = {
            'terms': Term.objects.all(),
            'relationships': Relationship.objects.all(),
            'licenses': License.objects.all(),
            'term': term,
            'term_rels': term.get_primary_relationships(),
        }
        return Response(params, template_name='vocab/edit_term.html',
                        status=status.HTTP_200_OK)
