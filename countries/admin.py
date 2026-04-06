from django.contrib import admin

from .models import City, Country, Language, Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "capital", "region", "population", "area")
    search_fields = ("name", "capital", "region")
    list_filter = ("region",)
    filter_horizontal = ("neighbors", "organizations")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "speakers_percent")
    search_fields = ("name", "country__name")
    list_filter = ("country",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "population")
    search_fields = ("name", "country__name")
    list_filter = ("country",)