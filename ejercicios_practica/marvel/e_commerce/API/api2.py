from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from e_commerce.models import *


@api_view(['GET','POST'])
@permission_classes([])
def api2(request):
    try:
        queryset = Comic.objects.filter(title=request.data.get("update_comic"))

        queryset.update(price=request.data.get("new_price_comic"))

        template = '<h1>Cambio exitoso!</h1>'
        
        return HttpResponse(template)
    
    except:
        template = '<h1>Error!</h1>' 
        return HttpResponse(template)