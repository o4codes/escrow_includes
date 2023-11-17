import re
from typing import Any, Callable, Iterable, Set, Union

from django.db import models
from rest_framework import serializers


def model_to_dict(
    instance: models.Model,
    exclude_fields: Set[str] = None,
) -> Union[dict, list]:
    """
    Convert a model instance to dict.
    """

    if exclude_fields is None:
        exclude_fields = set()
    exclude_fields = {
        field for field in exclude_fields if hasattr(instance, field)
    }

    class Serializer(serializers.ModelSerializer):

        class Meta:
            model = type(instance)
            depth = 1
            exclude = tuple(exclude_fields)

    serializer = Serializer(instance)
    return serializer.data


def only(func: Callable[[Any], bool], values: Iterable):
    """Checks if exactly only one item in values has truth

    Args:
        func:
        values (Iterable): iterable of values to check for

    Returns:
        bool: True if 1 else False
    """
    return len(list(filter(func(), values))) == 1


def slugify(
    text: str, replacement_char: str = "_", max_length: int = None
) -> str:
    """
    Normalizes a string by
    Removing all special characters and replacing with a specified character
    Changing all cases to lower case
    Truncating the resulting string to a specified maximum length
    """
    text = text.strip().lower()
    text = re.sub(r"[^\w\s]", replacement_char, text)
    text = re.sub(r"[\s]+", replacement_char, text)
    if max_length is not None and len(text) > max_length:
        text = text[:max_length]
    return text
