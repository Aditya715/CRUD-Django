"""
    Handler Views.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RequestListForm, UpdateStatusForm
from .models import RequestList

# Create your views here.
@login_required
def index(request):
    """
        Landing page --> Dashboard view function
    """
    context = {
        'queryset' : RequestList.objects.all()
    }
    return render(request, 'handler/index.html', context)

@login_required
def add_new(request):
    """
        Add new data to the handler database.
    """
    form = RequestListForm(request.POST or None)
    # checking validation
    if form.is_valid():
        request_id = form.cleaned_data.get('id')
        request_id = form.save().id
        return redirect(f'/update/{request_id}')

    return render(request, 'handler/add_new.html', {'form' : form})

@login_required
def update_existing(request, request_id):
    """
        Update an existing data in the database
    """
    data = RequestList.objects.get(pk=request_id)
    form = UpdateStatusForm(request.POST or None)

    context = {
        'form' : form,
        'data' : data 
    }

    # form validation here.
    if form.is_valid():
        status = form.cleaned_data.get('status')
        remarks = form.cleaned_data.get('remarks')
        data.status = status
        data.remarks = remarks
        data.save()
        return redirect(f'/view/{ request_id }')
    
    return render(request, 'handler/update.html', context)

@login_required
def view_data(request, request_id):
    """
        View Data View.
    """
    context = {
        'data' : RequestList.objects.get(pk=request_id)
    }
    
    return render(request, 'handler/view_data.html', context)