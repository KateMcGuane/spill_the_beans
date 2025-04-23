from django.shortcuts import render
from .models import TermsOfUse


# Create your views here.
def terms_of_use(request):
    terms = TermsOfUse.objects.all().order_by('-updated_on').first()
    return render(request, 'terms/terms_of_use.html', {'terms': terms})
