from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.throttling import UserRateThrottle

from chatbot.serializers.chat_serializer import ChatSerializer
from chatbot.utils import process_query


class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    throttle_classes = [UserRateThrottle]

    def post(self, request, format=None):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_query = serializer.validated_data['message']
            ip_address = request.META.get("REMOTE_ADDR")

            response_message = process_query(user_query)

            # vector_db = get_vector_db()
            # response_message = retrieve_from_vector_db(user_query, vector_db)

            return Response({'response': response_message})
        else:
            return Response(serializer.errors, status=400)
