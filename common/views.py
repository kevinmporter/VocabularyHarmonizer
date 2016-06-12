from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status


class MainView(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        params = {

        }
        return Response(params, template_name='common/main.html',
                        status=status.HTTP_200_OK)


class AboutView(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        params = {

        }
        return Response(params, template_name='common/about.html',
                        status=status.HTTP_200_OK)
