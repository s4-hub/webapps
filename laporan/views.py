from django.shortcuts import render, redirect
from .models import Company, Job
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
class ParseExcel(APIView):
    def post(self, request, format=None):
        try:
            excel_file = request.FILES['files']
        except MultiValueDictKeyError:
            return redirect('upload/')
        if (str(excel_file).split('.')[-1] == "xls"):
            data = xls_get(excel_file, column_limit=4)
        elif (str(excel_file).split('.')[-1] == "xlsx"):
            data = xlsx_get(excel_file, column_limit=4)
        else:
            return redirect('upload/')
            