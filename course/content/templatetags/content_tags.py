from django import template

register = template.Library()


@register.filter
def format_list_block(value):
    """Фильтр для преобразования текста в список"""
    if not value:
        return []

    lst = []
    ind = 1
    last_dg = 0
    while ind < len(value):
        if value[ind].isdigit():
            lst.append(value[last_dg:ind])
            last_dg = ind
        ind += 1
    lst.append(value[last_dg:])
    return lst


@register.filter
def get_item(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return None