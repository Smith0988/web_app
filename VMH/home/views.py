from django.shortcuts import render
from django.http import HttpResponse
from .main import *

def get_home(request):
    return render(request, 'home/home.html')


from django.http import JsonResponse


def perform_search(searchText, buttonId):
    if buttonId == "mainLinkButton":
        result = search_main_article_link(searchText)
    elif buttonId == "relatedLinkButton":
        result = search_related_article_link(searchText)
    elif buttonId == "allLinkButton":
        result = search_all_article_link(searchText)

    elif buttonId=="vhmSearchButton":
        result = search_sentence(searchText)

    elif  buttonId=="kvSearchButton":
        result = searc_kv(searchText)
    else:
        result = "Please check button"

    return result



def search(request):
    # Lấy giá trị từ ô input "searchText"
    results = []
    search_text = request.GET.get('searchText', '')

    # Lấy giá trị từ tham số 'buttonId'
    button_id = request.GET.get('buttonId', '')

    if search_text:
        results = perform_search(search_text, button_id)  # Điều này cần thay đổi dựa trên logic tìm kiếm của bạn
    else:
        results.append("Please input search text")

    # Trả về kết quả dưới dạng JSON
    return JsonResponse({"buttonId": button_id, "results": results})
