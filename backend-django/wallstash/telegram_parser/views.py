from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import parse


class ParseView(APIView):

    def post(self, request, *args, **kwargs):
        channel = request.data.get("channel")
        limit = request.data.get("limit")
        parse.delay(channel, limit)
        return Response({"status": "ok"})
