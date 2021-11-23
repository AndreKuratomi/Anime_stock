from flask import Blueprint
from app.controllers.app_controllers import blue_get_create, blue_get_all, blue_filter, blue_update, blue_delete


bp_animes = Blueprint('anime', __name__)

bp_animes.post("/animes")(blue_get_create)

bp_animes.get("/animes")(blue_get_all)

bp_animes.get("/animes/<int:anime_id>")(blue_filter)

bp_animes.patch("/animes/<int:anime_id>")(blue_update)

bp_animes.delete("/animes/<int:anime_id>")(blue_delete)
