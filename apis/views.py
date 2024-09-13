from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book
import requests
import openai

openai.api_key="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"
openai.organization = "org-jkyKjdm8k8dDE9YzPATtxhDu"

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChatAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_message = request.data.get('message')

        if not user_message:
            return Response("Provide a relevant message from user!", status=status.HTTP_400_BAD_REQUEST)
        
        prompt = f"User message: {user_message} \n Provide relavent response from api data."

        try:
            gpt_response = openai.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages= [{
                    "role": "user",
                    "content": prompt
                }],
                max_tokens=150
            )

            reply = gpt_response.choices[0].message.content

            return Response({'reply': reply})
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RandomUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get('https://randomuser.me/api/')
            response.raise_for_status()

            data = response.json()

            data = data['results']

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



