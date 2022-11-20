from django.shortcuts import render
from django.http import HttpResponse
import submit_url.db_interface as db

DB_PATH = './db.sqlite3'

# Create your views here.
def index(request):
    output_companies = {1: {'name': 'Microsoft'},
                        2: {'name': 'Facebook'},
                        3: {'name': 'Amazon'}}
    if request.method == "POST":
        company = request.POST['input_field']
        # TODO: some procesing of 'company' string
        try:
            sector, sector_id = db.getSector(DB_PATH, company)
        except:
            # display some alert saying that company wasn't found
            return render(request, "submit_url/index.html")
        print(sector)
        sector_companies = db.getSectorCompanies(DB_PATH, sector_id)
        print(sector_companies)
        # TODO: find most similar companies within sector companies
        return render(request, "submit_url/index.html", {
            "output_companies": sector_companies,
        })
    else:
        return render(request, "submit_url/index.html")