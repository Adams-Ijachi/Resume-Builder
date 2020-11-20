from rest_framework.decorators import api_view
from ..models import Template
from .serailizers import TemplateSerializer
from rest_framework.response import Response


@api_view(['GET'])
def template_list(request, *args, **kwargs):
    qs = Template.objects.all()
    serializer = TemplateSerializer(qs, many=True) 
    return Response(serializer.data)
# @api_view(['GET', 'POST'])
# def create_resume(request,*args, **kwargs):




    
