from django.shortcuts import render
from django.http import HttpResponse
from .main import *

def get_home(request):
    return render(request, 'home/home.html')

def search(request, method):
    results = []
    if request.method == 'POST':
        query = request.POST.get('query', '')

        if method == 'update':
            # Thực hiện tìm kiếm theo phương thức 'update'
            results = search_main_link(query)
        elif method == 'mainlink':
            # Thực hiện tìm kiếm theo phương thức 'mainlink'
            results = search_related_link(query)
        else:
            results = "Not found"
        # Xử lý các phương thức tìm kiếm khác ở đây

    return render(request, 'home/update.html', {'results': results})

