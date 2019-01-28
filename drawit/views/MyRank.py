import json
from django.http import HttpResponse
from drawit.models import *

def view(request, *args, **kwargs):

    stage_id = kwargs['stage_id']
    user_id = kwargs['user_id']

    queryset = BestRecord.objects.filter(stage_id=stage_id)
    myObject = queryset.get(user_id=user_id)

    rank = queryset.filter(record__lt = myObject.record).count()+1

    response_data = {}
    response_data['stage_id'] = stage_id
    response_data['user_id'] = user_id
    response_data['rank'] = rank
    response_data['record'] = myObject.record

    return HttpResponse(json.dumps(response_data), content_type="application/json")