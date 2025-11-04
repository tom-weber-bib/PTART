from django.db import models
from django.http import HttpRequest


def search_with_filter(qs: models.QuerySet, filters: dict[str, str], model: type[models.Model]) -> models.QuerySet:
    """
    Filter a Django queryset dynamically based on a dictionary of filters.
    """
    if not filters:
        return qs

    dynamic_filters = {}

    for field_name, field_value in filters.items():
        if field_value is None or not hasattr(model, field_name):
            continue

        field = model._meta.get_field(field_name)

        if isinstance(field, models.BooleanField):
            field_value = str(field_value).lower() in {"true", "1", "yes"}
        elif isinstance(field, models.CharField):
            field_name = f"{field_name}__icontains"

        dynamic_filters[field_name] = field_value

    if dynamic_filters:
        qs = qs.filter(**dynamic_filters)

    return qs


def get_filter_from_request(request: HttpRequest) -> dict[str, str]:
    """
    Extract non-empty GET parameters from an HttpRequest as a filter dictionary.
    """
    return {
        key: value
        for key, value in request.GET.items()
        if value not in {None, ""}
    }
