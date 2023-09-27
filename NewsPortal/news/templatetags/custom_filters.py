from django import template

register = template.Library()


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Должен быть текст!')

    nasty_list = [
        'редиска',
        'матрица',
        'цветы',
        'время',
        'место',
        'авто',
        'война'
    ]

    for item in nasty_list:
        if item in value.lower():
            c_index = value.lower().index(item)
            value = value.replace(value[c_index:c_index + len(item)], f"{value[c_index]}{'*' * (len(item) - 1)}")
    return value


@register.filter()
def new_censor(value):
    if not isinstance(value, str):
        raise ValueError('Должен быть текст!')

    forbidden_words = [
        'един',
        'росси',
        'матрица',
        'война',
        'робот',
        'отель'
    ]

    for i in forbidden_words:
        if i in value.lower():
            c_index = value.lower().index(i)
            value = value.replace(value[c_index + 1:c_index + len(i) - 1],
                                  f"{'*' * (len(i) - 2)}")
    return value
