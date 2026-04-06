from django.core.exceptions import ValidationError
from django.db import models


class Organization(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Country(models.Model):

    REGION_CHOICES = [
        ("Europe", "Europe"),
        ("Asia", "Asia"),
        ("Africa", "Africa"),
        ("North America", "North America"),
        ("South America", "South America"),
        ("Oceania", "Oceania"),
    ]

    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField()
    area = models.PositiveIntegerField(help_text="Area in square kilometers")
    region = models.CharField(max_length=30, choices=REGION_CHOICES)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    
    neighbors = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=True,
    )
    organizations = models.ManyToManyField(
        Organization,
        blank=True,
        related_name="countries",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Language(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="languages",
    )
    name = models.CharField(max_length=100)
    speakers_percent = models.PositiveIntegerField()

    class Meta:
        ordering = ["-speakers_percent", "name"]
        unique_together = ("country", "name")

    def clean(self):
        if self.speakers_percent > 100:
            raise ValidationError(
                {"speakers_percent": "Percentage cannot be greater than 100."}
            )

    def __str__(self):
        return f"{self.name} ({self.country.name})"


class City(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities",
    )
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()

    class Meta:
        ordering = ["-population", "name"]
        unique_together = ("country", "name")

    def __str__(self):
        return f"{self.name} ({self.country.name})"