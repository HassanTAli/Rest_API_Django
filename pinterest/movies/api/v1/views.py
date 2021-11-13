from django.http import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from .serializers import MovieSerializer
# from rest_framework.decorators import authentication_classes
# from rest_framework.authentication import TokenAuthentication


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hello(req,mykey):
    data = {'message':'Hell from rest api yor key is {}'.format(mykey)}
    if mykey == 'yes':
        return Response(data=data,status=status.HTTP_200_OK)
    else:
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def movie_list(req):
    movies = Movie.objects.all()
    serializer_Movie = MovieSerializer(instance=movies,many=True)
    return Response(data=serializer_Movie.data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_created(req):
    serializer_movie = MovieSerializer(data=req.data)
    if serializer_movie.is_valid():
        serializer_movie.save()
    else:
        return Response(data=serializer_movie.errors,status=status.HTTP_400_BAD_REQUEST)
    
    data = {
        'message':'Success',
        'data':{"id":serializer_movie.data.get('id')}
    }
    # return Response(data=serializer_movie.data,status=status.HTTP_201_CREATED)
    return Response(data=data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(req, pk):
    movie_Obj = Movie.objects.filter(pk=pk)
    if movie_Obj.exists():
        pass
    else:
        return Response(data={'message':'failed Movie doesnot exist'},status=status.HTTP_400_BAD_REQUEST)
        
    serialized_Movie = MovieSerializer(instance=movie_Obj)
    return Response(data=serialized_Movie.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def movie_delete(req,pk):
    response = {}
    try:
        movie_Obj = Movie.objects.get(pk=pk)
        movie_Obj.delete()
        response['data']={'message':'Successfully Deleted Movie'}
        response['status']=status.HTTP_200_OK
    except Exception as e:
        response['data']={'message':'Error during Deleted Movie {}'.format(str(e))}
        response['status']=status.HTTP_400_BAD_REQUEST
        
    return Response(**response)

@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
def movie_update(req,pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message': str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    if req.method == 'PUT':
        serialized_movie = MovieSerializer(instance=movie,data=req.data)
    elif req.method == 'PATCH':
        serialized_movie = MovieSerializer(instance=movie,data=req.data,partial=True)
        
    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data,status=status.HTTP_200_OK)
    return Response(data=serialized_movie.errors,status=status.HTTP_400_BAD_REQUEST)
    