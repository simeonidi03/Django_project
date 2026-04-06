from django.shortcuts import get_object_or_404, redirect, render
from .forms import CountryForm, TestAnswerForm
from .models import Country


def home(request):
    return render(request, "countries/home.html")


def country_list(request):
    countries = Country.objects.all()
    context = {"countries": countries}
    return render(request, "countries/country_list.html", context)

def country_detail(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    context = {"country": country}
    return render(request, "countries/country_detail.html", context)

def country_create(request):

    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save()
            return redirect("country_detail", country_id=country.id)
    else:
        form = CountryForm()

    context = {"form": form, "page_title": "Add country"}
    return render(request, "countries/country_form.html", context)


def country_edit(request, country_id):
    country = get_object_or_404(Country, pk=country_id)

    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save()
            return redirect("country_detail", country_id=country.id)
    else:
        form = CountryForm(instance=country)

    context = {"form": form, "page_title": f"Edit {country.name}"}
    return render(request, "countries/country_form.html", context)


def test_mode(request):
    """Redirect to the first available country test."""
    first_country = Country.objects.order_by("id").first()
    if first_country is None:
        return render(
            request,
            "countries/test_mode.html",
            {"country": None, "form": None, "result_message": None, "next_country": None},
        )
    return redirect("test_country", country_id=first_country.id)
    
def test_country(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    result_message = None

    if request.method == "POST":
        form = TestAnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data["answer"].strip().lower()
            correct_name = country.name.strip().lower()

            if answer == correct_name:
                result_message = "Correct!"
            else:
                result_message = f"Wrong answer. The correct answer is {country.name}."
    else:
        form = TestAnswerForm()

    next_country = (
        Country.objects.filter(id__gt=country.id).order_by("id").first()
    )
    if next_country is None:
        next_country = Country.objects.order_by("id").first()

    context = {
        "country": country,
        "form": form,
        "result_message": result_message,
        "next_country": next_country,
    }
    return render(request, "countries/test_mode.html", context)