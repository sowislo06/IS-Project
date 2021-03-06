from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CategoryForm, StationForm, AssetForm
from .models import Category, Station, Asset

def index(request):
    category_form = CategoryForm();
    station_form = StationForm();
    asset_form = AssetForm();
    categories = Category.objects.order_by('name')
    stations = Station.objects.order_by('name')
    assets = Asset.objects.order_by('name')

    return render(request, 'asset/dashboard.html', {'category_form': category_form, 'categories': categories, 'station_form': station_form,
                                                    'asset_form': asset_form, 'stations': stations, 'assets': assets })


@login_required
@require_POST
def create_category_view(request):
    category_form = CategoryForm(request.POST)
    if category_form.is_valid():
        category_form.save()
    return HttpResponseRedirect(reverse('asset:index'))

@login_required
@require_POST
def create_station_view(request):
    station_form = StationForm(request.POST)
    if station_form.is_valid():
        station_form.save()
    return HttpResponseRedirect(reverse('asset:index'))

@login_required
@require_POST
def create_asset_view(request):
    asset_form = AssetForm(request.POST)
    if asset_form.is_valid():
        asset_form.save()
    return HttpResponseRedirect(reverse('asset:index'))


@login_required
def select_station_view(request, station_id):
    asset = Asset.objects.filter(station_id=station_id)
    station = Station.objects.get(pk=station_id)
    return render(request, 'asset/station.html', {'asset': asset, 'station': station})
