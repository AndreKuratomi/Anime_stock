from flask import request
from app.models.app_models import Animes
from exceptions.app_exceptions import InvalidKeysError, NotFoundError
from psycopg2.errors import UniqueViolation
from ipdb import set_trace


valid_keys = {"anime", "released_date", "seasons"}


def blue_get_create():
    try:
        data = request.json

        data_keys = data.keys()
        data_set = set(data_keys)
        comparison = data_set.difference(valid_keys)

        list_for_exception = []
        for elts in comparison:
            list_for_exception.append(elts)

        if comparison != set():
            raise InvalidKeysError(list_for_exception)

        else:
            new_object = Animes(**data)
            new_anime = new_object.create()
            return new_anime, 201

    except InvalidKeysError as ike:
        return ike.message, 422

    except UniqueViolation:
        return {'error': 'anime is already exists'}, 409


def blue_get_all():
    all_animes = Animes.get_all()
    if len(all_animes) > 0:
        return {"data": all_animes}, 200
    return {"data": []}, 200


def blue_filter(anime_id):
    try:
        filtering = Animes.filter(anime_id)
        return {"data": filtering}, 200

    except NotFoundError as nfe:
        return nfe.message, 404


def blue_update(anime_id):
    try:
        data = request.json

        data_keys = data.keys()
        data_set = set(data_keys)
        comparison = data_set.difference(valid_keys)

        list_for_exception = []
        for elts in comparison:
            list_for_exception.append(elts)

        if comparison != set():
            raise InvalidKeysError(list_for_exception)

        else:
            to_update = Animes.update(data, anime_id)
            return to_update, 201

    except NotFoundError as nfe:
        return nfe.message, 404

    except InvalidKeysError as ike:
        return ike.message, 422


def blue_delete(anime_id):
    try:
        Animes.filter(anime_id)
        Animes.delete(anime_id)
        return '', 204

    except NotFoundError as nfe:
        return nfe.message, 404
