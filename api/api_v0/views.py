from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import Serializer

from .serializers import FortuneSerializer


class FortuneView(GenericAPIView):
    serializer_class = FortuneSerializer

    def post(self, request):
        serializer: Serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
