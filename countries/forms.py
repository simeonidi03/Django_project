from django import forms

from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            "name",
            "capital",
            "population",
            "area",
            "region",
            "description",
            "neighbors",
            "image_url",
            "organizations",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "neighbors": forms.CheckboxSelectMultiple(),
            "organizations": forms.CheckboxSelectMultiple(),
            "image_url": forms.URLInput(attrs={"placeholder": "https://example.com/image.jpg"}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError(
                "Country name must contain at least 2 characters."
            )
        return name

    def clean_capital(self):
        capital = self.cleaned_data["capital"].strip()
        if len(capital) < 2:
            raise forms.ValidationError(
                "Capital name must contain at least 2 characters."
            )
        return capital


class TestAnswerForm(forms.Form):
    answer = forms.CharField(
        max_length=100,
        label="Your answer",
        help_text="Enter the country name.",
        error_messages={"required": "Please enter a country name."},
    )

    def clean_answer(self):
        answer = self.cleaned_data["answer"].strip()
        if len(answer) < 2:
            raise forms.ValidationError(
                "The answer must contain at least 2 characters."
            )
        return answer