from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from .serializers import AnalysisSerializer
from .AccessYoutubeComment import start
from .AccessYoutubeComment import data


class CommentAnalysis(APIView):

    def get(self,request,video_id):
        """
        Return if overall comment is negative or positive
        """
        temp = start(video_id)
        serializer = AnalysisSerializer(temp,many=True)
        return Response(serializer.data)

