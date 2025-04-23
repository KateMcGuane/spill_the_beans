from django.shortcuts import render
from .models import TermsOfUse


# Create your views here.
def terms_of_use(request):
    """
    Renders the most recent information on the website Terms of Use.

    Retrieves the most recent instance of :model:`terms.TermsOfUse` and
    displays its content to the user. This view is intended to present the
    latest legal or policy terms applicable to site usage.

    **Context**
    ``terms``
        The most recent instance of :model:`terms.TermsOfUse`, ordered by
        the latest update timestamp.

    **Template**
    :template:`terms/terms_of_use.html`
        Displays the Terms of Use content in a formatted layout.
    """
    terms = TermsOfUse.objects.all().order_by('-updated_on').first()
    return render(request, 'terms/terms_of_use.html', {'terms': terms})
