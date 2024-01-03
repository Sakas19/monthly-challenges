from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "New Year, New Skill",
    "february": "Random Acts of Kindness",
    "march": "30-Day Fitness Challenge",
    "april": "Spring Cleaning and Decluttering",
    "may": "Read a Book a Week",
    "june": "Digital Detox",
    "july": "Healthy Eating and Cooking",
    "august": "Outdoor Adventure",
    "september": "Learn Something New",
    "october": "Gratitude Journal",
    "november": "Giving Back",
    "december": "Random Acts of Holiday Kindness"
}

# Create your views here.

def index(request):
    list_item = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try: 
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")