from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from e_commerce.models import *


@api_view(['GET','POST'])
@permission_classes([])
def api3(request):
    try:
        queryset = Comic.objects.filter(title=request.data.get("delete_comic"))

        queryset.delete()

        template = '<h1>Borrado exitoso!</h1>'
        
        return HttpResponse(template)
    
    except:
        template = '<h1>Error!</h1>' 
        return HttpResponse(template)