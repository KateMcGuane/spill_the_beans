from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Retrieves the most recent instance of :model:`about.About` and
    handles form submissions for collaboration request. Upon a succesful
    form submission, the request is saved and a success message is shown.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`,
        either pre-populated or empty.

    **Template**
    :template:`about/about.html`
        Renders both the about information & collboration form.
    """
    about = About.objects.all().order_by('-updated_on').first()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_request = collaborate_form.save(commit=False)
            collaborate_request.read = False
            collaborate_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                ('Collaboration request received! I endeavor to respond '
                 'within 2 working days.')
            )
            collaborate_form = CollaborateForm()
        else:
            collaborate_form = CollaborateForm()
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
