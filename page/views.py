from django.shortcuts import render, get_object_or_404
from .models import BranchLocation

def home_page(request):
    branches = BranchLocation.objects.all()
    return render(request, 'base.html', {'branches': branches})

def branch_detail(request, pk):
    branch = get_object_or_404(BranchLocation, pk=pk)
    return render(request, 'branch_detail.html', {'branch': branch})