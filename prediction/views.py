from django.http import HttpResponseBadRequest
from django.views.generic.edit import FormView
from django.views.decorators.http import require_http_methods

from .forms import AvocadoDataForm
from .serializers import AvocadoDataSerializer


class AvocadoDataFormView(FormView):
    template_name = 'prediction/predict.html'
    form_class = AvocadoDataForm


@require_http_methods(["POST"])
def predict(request):
    form = AvocadoDataForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()

    serializer = AvocadoDataSerializer(data=form.cleaned_data)
    if not serializer.is_valid():
        return HttpResponseBadRequest()

    prediction = serializer.data.get('sold_plu_4046') + serializer.data.get('sold_plu_4225') + 2*serializer.data.get('small_bags') + 1000
    context = {'predicted_average_price': prediction, 'form': form}

    return AvocadoDataFormView(request=request).render_to_response(context)