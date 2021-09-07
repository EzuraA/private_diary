from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import InquiryForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

class IndexView(generic.TemplateView):
    template_name="Index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    