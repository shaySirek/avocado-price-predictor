from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.decorators.http import require_http_methods

from .models import AvocadoData 
from .forms import AvocadoDataForm
from .serializers import AvocadoDataSerializer


class AvocadoDataFormView(FormView):
    template_name = 'prediction/predict.html'
    form_class = AvocadoDataForm


@require_http_methods(["POST"])
def predict(request):
    data = {field: request.POST.get(field) for field in AvocadoDataForm.Meta.fields}
    data['organic'] = data['organic'] or False

    serializer = AvocadoDataSerializer(data=data)
    if serializer.is_valid():
        prediction = serializer.data.get('sold_plu_4046') + serializer.data.get('sold_plu_4225') + 2*serializer.data.get('small_bags') + 1000

        context = {'predicted_average_price': prediction}
        input_type = {'int': 'number', 'bool': 'checkbox', 'str': 'text'}
        context['form'] = [ 
            { 
                'auto_id': "id_{}".format(k),
                'name': k,
                'label': k.replace("_", " "),
                'data': v,
                'widget_type': input_type[type(v).__name__]
            }
            for k,v in serializer.data.items()]

        return render(request, AvocadoDataFormView.template_name, context)

    return HttpResponseBadRequest()