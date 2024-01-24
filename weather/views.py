from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from .models import City
from .forms import CityForm, ChoiceForm
from .utils import get_city_data_by_coordinates, get_city_options, create_records


class IndexView(View):
    def get(self, request):
        """When method is GET render currentweather_index.html template."""

        return render(request, "weather/index.html", {"form": CityForm()})

    def post(self, request):
        """When method is Post get request parameters, get a list of matches and show matches in choice form. If only one match is found, create records and redirect to details page for match.
        If choice form was submitted, create records and redirect to details page for choice.
        """
        
        if (request.POST.get("choice")) != None:
            choice = request.POST.get("choice").split(" ")
            create_records(
                city_id := int(choice[0]),
                units=choice[1],
                state=choice[2] if len(choice) == 3 else None,
            )
            return redirect("detail", pk=city_id)

        else:
            form = CityForm(request.POST)
            if (
                not form.is_valid()
                or len(
                    options := get_city_options(
                        city=form.cleaned_data["city"],
                        country_code=form.cleaned_data["country"],
                    )
                )
                == 0
            ):
                return render(request, "weather/index.html", {"nonefound": True})

            units = form.cleaned_data["units"]

            for option in options:
                data = get_city_data_by_coordinates(
                    lat=option.get("lat"), lon=option.get("lon"), units=units
                )
                option.update({"city_id": data.get("id"), "units": units})

            if len(options) == 1:
                create_records(
                    city_id := options[0].get("city_id"),
                    units=units,
                    state=options[0].get("state"),
                )
                return redirect("detail", pk=data.get("id"))

            else:
                return render(
                    request,
                    "weather/index.html",
                    {
                        "options": options,
                        "units": units,
                        "form": form,
                        "choices": ChoiceForm(options=options),
                    },
                )


class CityDetailView(DetailView):
    model = City

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Update context data to include current and daily weather data."""

        context = super().get_context_data(**kwargs)
        city = self.get_object(self.get_queryset())
        context["daily_data"] = city.get_daily_data()
        context["current_data"] = city.get_current_data()
        return context
