"""Views for main end."""


from django.shortcuts import render


def home_view(request):
    """Home route is requested."""
    return render(request, 'home.html')
