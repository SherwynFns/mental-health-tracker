from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165811',
        'name': 'A. Sherwyn Fawwaz Nitisara Suthaputra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)