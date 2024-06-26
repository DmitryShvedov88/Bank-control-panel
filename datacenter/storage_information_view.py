from django.shortcuts import render
from datacenter.calculating_visit_time import get_duration
from datacenter.models import Visit


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [
        {"who_entered": str(visit.passcard),
         "entered_at": str(visit.entered_at),
         "duration": get_duration(visit)
         }
        for visit in visits
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
