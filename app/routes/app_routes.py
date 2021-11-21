from flask import Flask
from app.controllers.app_controllers import blue_get_create, blue_filter, blue_update, blue_delete


def init_app(app: Flask):

    app.get("/animes")(blue_get_create())
    app.post("/animes")(blue_get_create())
    app.get("/animes/<int:anime_id>")(blue_filter())
    app.patch("/animes/<int:anime_id>")(blue_update())
    app.delete("/animes/<int:anime_id>")(blue_delete())
