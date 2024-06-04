from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Simple view for the root path
def home(request):
    return HttpResponse("Hello, this is the home page.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', home),  # Root path
    path('favicon.ico', lambda x: HttpResponse('Favicon not found', content_type='image/x-icon')),  # Favicon
]

    
