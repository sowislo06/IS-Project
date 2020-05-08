from django.shortcuts import render, reverse
from .forms import ActivityForm, AssetForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Activity
from django.utils import timezone
from asset.models import Station, Asset
from django.template.defaulttags import register

def index(request):
    activity_form = ActivityForm()
    activities = Activity.objects.order_by('startDate')
    return render(request, 'logistics/base.html', {'activity_form': activity_form, 'activities': activities})

@login_required
@require_POST
def create_activity_view(request):
    activity_form = ActivityForm(request.POST)
    if activity_form.is_valid():
        #In dem Fall, wenn eine Activity angelegt wird und dem Asset bereits eine Acitivity zugeordnet ist, wird das Enddatum automtisch gesetzt
        if Activity.objects.filter(asset=activity_form.cleaned_data['asset']).exists():
            if Activity.objects.filter(asset=activity_form.cleaned_data['asset']).get(endDate = None):
                p = Activity.objects.filter(asset=activity_form.cleaned_data['asset']).get(endDate = None)
                p.endDate=timezone.now()
                p.save()
        activity = activity_form.save(commit=False)
        activity.user = request.user
        activity_form.save()
        #Station in der Tabelle "Asset" ändern
        Asset.objects.filter(pk=activity_form.cleaned_data['asset'].id).update(station=activity_form.cleaned_data['station'])
    return HttpResponseRedirect(reverse('logistics:index'))

def select_activity_view(request):
    asset_form = AssetForm()
    activities = None
    if request.method == 'POST':
        asset_form = AssetForm(request.POST)
        if asset_form.is_valid():
            activities = Activity.objects.filter(asset=asset_form.cleaned_data['asset']).all()

    return render(request, 'logistics/activities.html', {'asset_form': asset_form, 'activities': activities})

def overview_view(request):
    activities = Activity.objects.all()
    sumStations = Station.objects.all()
    assets = Asset.objects.all()


    return render(request, 'logistics/dashboard.html', {'activities': activities, 'sumStations': sumStations, 'assets': assets})

