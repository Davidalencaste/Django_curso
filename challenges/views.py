from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Learn Django for at least 20 minutes every day!"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge",args = [month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    return HttpResponse(response_data)