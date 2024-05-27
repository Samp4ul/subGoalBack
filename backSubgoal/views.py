# myapp/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import Score, Subgoal

# Replace this with your actual token value
BEARER_TOKEN = "1klAj7wCVgJCx6F7c7u5Oqwrlzlh1gyuK6O2Dj9HXb2mJFUA2c"

def verify_bearer_token(request):
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        return token == BEARER_TOKEN
    return False

@api_view(['GET'])
@permission_classes([AllowAny])
def verify(request):
    if verify_bearer_token(request):
        return Response({"message": "Token Verified"}, status=status.HTTP_200_OK)
    return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def modify_point(request):
    if not verify_bearer_token(request):
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        score_actuel = request.data.get('score_actuel')
        if not Score.objects.exists():
            Score.objects.create(score_actuel=score_actuel)
        else:
            score_instance = Score.objects.first()
            score_instance.score_actuel = score_actuel
            score_instance.save()
        return Response({"message": "Score Updated"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_subgoal(request):
    if not verify_bearer_token(request):
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        nom = request.data.get('nom')
        score = request.data.get('score')
        description = request.data.get('description')
        Subgoal.objects.create(nom=nom, score=score,description=description)
        return Response({"message": "Subgoal Created"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_data(request):
    # Retrieve the current score
    score = Score.objects.first()
    score_actuel = score.score_actuel if score else 0

    # Retrieve all subgoals
    subgoals = Subgoal.objects.all().values('score', 'nom','description')

    return Response({
        "score_actuel": score_actuel,
        "subgoals": list(subgoals)
    }, status=status.HTTP_200_OK)