from django.shortcuts import render, get_object_or_404

from inventory.models import Element, Project


def index(request):
    return render(request, 'index.html', context=None)


def project_elements(request, project_id: int = 0):
    projects = Project.objects.filter(visible=True)
    print(project_id)
    try:
        parent_project = Project.objects.values_list().get(id=project_id)
        elements = Element.objects.filter(parent_project=parent_project)
    except Project.DoesNotExist:
        parent_project = None
        elements = None

    context = {
        'projects': projects,
        'elements': elements,
    }

    return render(request, 'inventory/project_elements.html', context=context)
