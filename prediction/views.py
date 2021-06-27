from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from json import loads
from .forms import AvocadoDataForm
from .serializers import AvocadoDataSerializer
from avocado_price_predictor_model import predict as predictor
from datetime import datetime


@require_http_methods(["POST"])
def predict(request):
    form = AvocadoDataForm(loads(request.body.decode("utf-8")))
    if not form.is_valid():
        return HttpResponseBadRequest()

    serializer = AvocadoDataSerializer(data=form.cleaned_data)
    if not serializer.is_valid():
        return HttpResponseBadRequest()

    data = dict(serializer.data)
    data['date'] = datetime.now().strftime('%Y-%m-%d')

    prediction = predictor.predict(data)

    return JsonResponse({'predicted_average_price': prediction})


@require_http_methods(["GET"])
def default(request):
    return JsonResponse({f: "" for f in AvocadoDataForm.Meta.fields})