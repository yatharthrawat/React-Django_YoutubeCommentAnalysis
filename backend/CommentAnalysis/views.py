from rest_framework import generics
# Create your views here.

from .models import Analysis
from .serializers import AnalysisSerializer

class CommentAnalysis(generics.ListCreateAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer


class Analysis(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

