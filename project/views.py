import math
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework import permissions
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import re
import math
import re
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .serializers import ProjectSerializer



def index(request):
    return render(request, 'index.html')


# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def halstead_metrics(text):
    operators = re.findall(r'(\+\+|--|\+=|-=|\*=|/=|%=|\|=|&=|\^=|<<=|>>=|!=|==|>=|<=|>|<|\|\||&&|\?|:|~|\||&|\^|<<|>>|\!|\=|\+|-|\*|/|%|\.|\,|\;|\(|\)|\[|\]|\{|\}|\#\w+|\w+)', text)
    operands = re.findall(r'(\b\d+\b|[A-Za-z_]\w*)', text)

    n1 = len(set(operators))
    n2 = len(set(operands))
    N = len(operators) + len(operands)

    # Handle division by zero error
    if n1 == 0 or n2 == 0:
        V = 0
        D = 0
    else:
        V = N * math.log2(n1 + n2)
        D = (n1 / 2) * (n2 / n1)

    E = V * D
    T = E / 18
    cost = V / 3000

    return {
        'n1': n1,
        'n2': n2,
        'N': N,
        'V': round(V, 2),  # Round V to 2 decimal places
        'D': round(D, 2),  # Round D to 2 decimal places
        'E': round(E, 2),  # Round E to 2 decimal places
        'T': round(T, 2),   # Round T to 2 decimal places
        'cost': round(cost, 2)
    }

class CompareCodes(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            file1 = request.FILES.get('file1')
            file2 = request.FILES.get('file2')

            # Read the content of file1 and file2
            content1 = file1.read().decode('utf-8')
            content2 = file2.read().decode('utf-8')

            # Compute Halstead metrics for file1 and file2
            metrics1 = halstead_metrics(content1)
            metrics2 = halstead_metrics(content2)

            # Compare the metrics
            if metrics1['E'] < metrics2['E']:
                winner = 'File 1'
                loser = 'File 2'
            elif metrics1['E'] > metrics2['E']:
                winner = 'File 2'
                loser = 'File 1'
            else:
                winner = 'Both files are equally complex'
                loser = ''

            # Prepare the response data
            response_data = {
                'success': 'Comparison successful',
                'metrics1': metrics1,
                'metrics2': metrics2,
                'winner': winner,
                'loser': loser
            }

            return JsonResponse(response_data)

        return JsonResponse({'error': 'Invalid input'})
