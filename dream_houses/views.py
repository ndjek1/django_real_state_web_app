from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
	properties = Property.objects.all()
	#Home page for learning logs
	return render(request, 'dream_houses/index.html', {'properties':properties})
@login_required
def dashboard(request):
	properties = Property.objects.filter(owner=request.user).order_by('date_added')
	#Home page for learning logs
	return render(request, 'dream_houses/dashboard.html', {'properties':properties})

@login_required
def new_property(request):
    if request.method != 'POST':
        form = PropertyForm()
    else:
        # Post data submitted, process data
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            new_property = form.save(commit=False)
            new_property.owner = request.user
            new_property.save()
            return redirect('dream_houses:dashboard')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'dream_houses/new_property.html', context)



def edit_property(request, property_id):
    property_instance = Property.objects.get(id=property_id)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('dream_houses:dashboard')
    else:
        form = PropertyForm(instance=property_instance)

    context = {'property': property_instance, 'form': form}
    return render(request, 'dream_houses/edit_property.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out.')
    return redirect('dream_houses:index')