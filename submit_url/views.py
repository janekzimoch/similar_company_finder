from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    output_companies = {1: {'name': 'Microsoft'},
                        2: {'name': 'Facebook'},
                        3: {'name': 'Amazon'}}
    if request.method == "POST":
        print(request.POST['input_field'])
        return render(request, "submit_url/index.html", {
            "output_companies": output_companies,
        })
    else:
        return render(request, "submit_url/index.html")