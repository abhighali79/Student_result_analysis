from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    dictionary[key]
    return dictionary.get(str(key), "N/A")

@register.filter
def get_item1(dictionary, key):
    dictionary[key]
    return dictionary.get(key, "N/A")
@register.filter
def get_item3(dictionary, key):
    print(dictionary)
    dictionary[key]
    return dictionary.get(key, "N/A")

@register.filter
def get_item2(dictionary, key):
    return dictionary.get(key, {'internal': 0, 'external': 0, 'total': 0})
@register.filter
def get_nested_item(dictionary, key_chain):
    """
    Safely retrieves a nested item from a dictionary.
    The key_chain should be a string with keys separated by dots (e.g., "MATH101.internal").
    """
    try:
        keys = key_chain.split('.')
        for key in keys:
            dictionary = dictionary.get(key, {})
        return dictionary
    except (AttributeError, KeyError, TypeError):
        return None
