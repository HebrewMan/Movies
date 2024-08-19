from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.decorators import action


from movie.models import Movie
from movie.serializers import MovieSerializer
from account.models import Profile


# Create your views here.
class CollectViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        movies = profile.movies.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        profile = Profile.objects.get(user=user)
        movie_id = request.data['movie_id']
        try:
            movie = Movie.objects.get(id=movie_id)
            profile.movies.add(movie)
            return Response({
                'status_code': 0,
                'message': '收藏成功'
                })
        except ObjectDoesNotExist:
            return Response({
                'status_code': 10001,
                'message': '电影信息不存在'
                })
        except:
            return Response({'message': '收藏失败'})

    def destroy(self, request, pk):
        user = request.user
        profile = Profile.objects.get(user=user)
        try:
            movie = Movie.objects.get(id=pk)
            if movie not in profile.movies.all():
                return Response({'message': '没有收藏这个电影'})
            profile.movies.remove(movie)
            return Response({'status_code':0,
                             'message': '取消收藏成功'})
        except ObjectDoesNotExist:
            return Response({'message': '电影信息不存在'})
        except:
            return Response({'message': '取消收藏失败'})
        
    @action(detail=True, methods=['get'])
    def is_collected(self, request, pk=None):
        user = request.user
        profile = Profile.objects.get(user=user)
        movie = Movie.objects.get(id=pk)
        is_collected = profile.movies.filter(id=movie.id).exists()
        return Response({'is_collected': is_collected})
        