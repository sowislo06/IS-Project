from django.shortcuts import render, reverse
from .forms import ActivityForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Activity
from django.utils import timezone

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

    return HttpResponseRedirect(reverse('logistics:index'))
