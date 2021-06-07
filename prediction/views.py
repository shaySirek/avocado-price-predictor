from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import AvocadoData 
from .forms import AvocadoDataForm
from .serializers import AvocadoDataSerializer


class AvocadoDataFormView(FormView):
    template_name = 'prediction/predict.html'
    form_class = AvocadoDataForm


def predict(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed", status=405)

    data = {field: request.POST.get(field) for field in AvocadoDataForm.Meta.fields}
    serializer = AvocadoDataSerializer(data=data)
    if serializer.is_valid():
        prediction = serializer.data.get('sold_plu_4046') + serializer.data.get('sold_plu_4225') + 2*serializer.data.get('small_bags') + 1000

        context = {'predicted_average_price': prediction}
        context['data'] = { k.replace("_", " "): v for k,v in serializer.data.items()}
        return render(request, AvocadoDataFormView.template_name, context)

    return JsonResponse(serializer.errors, status=400)    