from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Shield',
        'name': 'Anders Willard Leo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)