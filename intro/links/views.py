from django.shortcuts import render

# Create your views here.
def first(request):
    return render(
        request,
        'links/first.html'
    )


def second(request):
    return render(
        request,
        'links/second.html'
    )