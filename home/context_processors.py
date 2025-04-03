def menu_context(request):
    menu_items = [
        # {'name': 'RR', 'url': '/', 'class': 'main-btn'},
        # {'name': 'Новости', 'url': '/news'},
        # {'name': 'Концерты', 'url': 'https://without-events.ru/viperr_show', 'target': "_blank"},
        # {'name': 'Мерч', 'url': '/merch'},
        # {'name': 'Снипеты', 'url': '/snippets'},
    ]
    return {
        'menu_items': menu_items,
        'me': request.user,
    }