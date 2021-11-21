from app.models.app_models import Animes


def blue_get_create():
    return Animes.get_create()


def blue_filter():
    return Animes.filter()


def blue_update():
    return Animes.update()


def blue_delete():
    return Animes.delete()
