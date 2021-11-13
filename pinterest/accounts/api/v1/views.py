from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([])
def signup(req):
    data = {'data':'','status':''}
    user_serialized = UserSerializer(data=req.data)
    
    if user_serialized.is_valid():
        user_serialized.save()
        data['data'] = {
            'user':{
                'email':user_serialized.data.get('email'),
                'username':user_serialized.data.get('username')
                },
            'message':'Created'
        }
        data['status']=status.HTTP_201_CREATED
    else:
        data['data']=user_serialized.errors
        data['status']=status.HTTP_400_BAD_REQUEST
    # print('======>', user_serialized.data)
    
    return Response(**data)