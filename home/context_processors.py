def menu_context(request):
    return {
        'me': request.user,
    }