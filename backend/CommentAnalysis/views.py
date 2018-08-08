from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from .serializers import AnalysisSerializer

class CommentAnalysis(APIView):

    def get(self,request,video_id):
        """
        Return if overall comment is negative or positive
        """
        temp="pos "+video_id

        return Response(temp)

