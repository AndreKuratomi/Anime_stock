from app.models.app_models import Animes


def blue_get_create():
    data = request.json()
    new_object = Animes(**data)
    new_object.get_create()
    return new_object, 201


def blue_filter():
    filtering = Animes.filter()
    return filtering, 200


def blue_update():
    updated = Animes.update()
    return updated, 200


def blue_delete():
    deleted = Animes.delete()
    return deleted, 200
