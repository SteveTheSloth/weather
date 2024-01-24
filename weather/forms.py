from django import forms


class CityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields["city"].widget.attrs["placeholder"] = "City"
        self.fields["country"].widget.attrs[
            "placeholder"
        ] = "Counry Code (e.g. GB - optional)"

    city = forms.CharField(required=True, max_length=100)
    country = forms.CharField(required=False, max_length=100)
    units = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices={"standard": "Standard", "metric": "Metric", "imperial": "Imperial"},
        initial="standard",
    )


class ChoiceForm(forms.Form):
    def __init__(
        self,
        options=None,
        *args,
        **kwargs,
    ):
        super(ChoiceForm, self).__init__(*args, **kwargs)

        if options:
            choice_dict = {}
            for option in options:
                if option.get("state"):
                    choice_key = (
                        str(option.get("city_id"))
                        + " "
                        + option.get("units")
                        + " "
                        + option.get("state")
                    )

                    choice_dict[choice_key] = (
                        option.get("name")
                        + ", "
                        + option.get("state")
                        + ", "
                        + option.get("country")
                    )
                else:
                    choice_dict[
                        str(option.get("city_id")) + " " + option.get("units")
                    ] = (option.get("name") + ", " + option.get("country"))
            self.fields["choice"] = forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=choice_dict,
                initial=[options[0].get("city_id")],
            )
            
            # for field in self.fields
