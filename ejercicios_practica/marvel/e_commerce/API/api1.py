from rest_framework.decorators import api_view
from django.http import HttpResponse
from e_commerce.models import *


@api_view(['GET'])
def api1(request):
    try:
        queryset = Comic.objects.all()
        comic_name = {}
        title_list = []
        i = 0

        while True:        
            comic_name['title'] = queryset[i].title
            
            if comic_name('title') is None:
                break

            title_list.append(comic_name)

            i=+1

        return HttpResponse(title_list)
    
    except:
        template = '<h1>Error!</h1>' 
        return HttpResponse(template)