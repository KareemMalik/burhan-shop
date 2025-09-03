from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406348710',
        'name': 'Malik Alifan Kareem',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)