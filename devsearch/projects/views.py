from django.shortcuts import render
from django.http import HttpResponse

project_List = [
    {
        'id': '1',
        'title': "Ecom WWebsite",
        'description': 'Fully functional ecom website',\
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'Fully functional ecom website'
    },
    {
        'id': '3',
        'title': "Social Network Website",
        'description': 'Awesome open source project'

    },

]


def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': project_List}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_obj = None
    for i in project_List:
        if i['id'] == pk:
            project_obj = i
    return render(request, 'projects/single-project.html', {'project': project_obj})
