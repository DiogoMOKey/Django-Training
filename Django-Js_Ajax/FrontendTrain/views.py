from rest_framework.permissions import AllowAny
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

''' Templates

HomePageView
PikaPageView
AjaxGetDetailView


''' 

class HomePageView(TemplateView):   
    template_name = "home.html"
    
    
class PikaPageView(TemplateView):   
    template_name = "pika.html"
    
    
class AjaxGetDetailView(TemplateView):
    template_name = "ajax_get_detail.html"
    
    
class AjaxHandleFormView(TemplateView):
    template_name = "ajax_handle_form.html"   
    
    
class AjaxHandlerView(View):
    # Simple Ajax View
    def get(self, request):
        text = request.GET.get('button_text')
        
        if is_ajax(request=request):
            t = datetime.now()
            return JsonResponse({'seconds': t}, status=200)
        
        return render(request, 'ajax.html')
    
    def post(self, request):
        card_text = request.POST.get('text')
        result = f"I've got: {card_text}"
        return JsonResponse({'data': result}, status=200)
    

class ApiMovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def _get_filter(self): 
        # Test Filters on list
        filters = {
            'movie_id': 0,
        }
        
        try: 
            movie = self.request.query_params.get('movie_id')
        except:
            raise

        if movie and movie > 0:
            filters['movie_id'] = movie
        return filters
    
    def list(self, request):
        # Get List of Movies
        filters = self._get_filter()
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        response = Response(serializer.data)
        return response
    
    def retrieve(self, request, pk=None):
        # Get Details of a single Movie
        try:
            test_pk = int(pk)
            id = pk
        except:
            raise
        movie = self.queryset.get(id=id)
        serializer = self.serializer_class(movie)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        # Create a single Movie
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, pk=None):
        # Update a single Movie
        movie = self.get_object()
        serializer = self.get_serializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def count_movies(request):
    # Api Get Data
    count = {
        'movies_count': Movie.objects.count(),
    }
    return Response(count, status=200)