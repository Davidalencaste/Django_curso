from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges_dict.keys())
    
    return render(request,"challenges/index.html",{
        "months": months        
    })


def monthly_challenges_int(request, month):
    months = list(monthly_challenges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")
    redirect_month = months[month -1]
    redirect_path = reverse("month_challenge", args=[redirect_month]) ## reverse is used to get the URL path for the month_challenge view
    return HttpResponseRedirect(redirect_path)    

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name":month
        })
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        raise Http404()
    