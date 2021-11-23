# from flask import Blueprint
from dotenv import load_dotenv
from os import getenv
import psycopg2
from ipdb import set_trace

from exceptions.app_exceptions import NotFoundError

load_dotenv()

configs = {
    "host": getenv("HOST"),
    "database": getenv("DATABASE"),
    "user": getenv("USER"),
    "password": getenv("PASSWORD")
}


class Animes:

    fieldnames = ['id', 'anime', 'released_date', 'seasons']

    def __init__(self, anime: str, released_date: str, seasons: int) -> None:
        self.anime = anime.title()
        self.released_date = released_date
        self.seasons = seasons

    @staticmethod
    def create_table():
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS animes(
                    id 			  BIGSERIAL    PRIMARY KEY,
                    anime 		  VARCHAR(100) NOT NULL UNIQUE,
                    released_date DATE 		   NOT NULL,
                    seasons 	  INTEGER 	   NOT NULL
                );
            """
        )

        conn.commit()
        cur.close()
        conn.close()

    def create(self):

        Animes.create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        query = """
                    INSERT INTO animes (anime, released_date, seasons)
                    VALUES (%s, %s, %s)
                    returning *;
                """
        anime_values = list(self.__dict__.values())
        cur.execute(query, anime_values)

        raw_anime = cur.fetchone()
        ready_anime = dict(zip(self.fieldnames, raw_anime))

        conn.commit()
        cur.close()
        conn.close()

        return ready_anime

    @staticmethod
    def get_all():

        Animes.create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute(
            """
                SELECT * FROM animes
            """
        )

        show_animes = cur.fetchall()
        result = [dict(zip(Animes.fieldnames, line)) for line in show_animes]
        # set_trace()

        conn.commit()
        cur.close()
        conn.close()

        return result

    @staticmethod
    def filter(id):

        Animes.create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()
        try:
            cur.execute(
                """
                    select * from animes where id=%s
                """,
                (id,)
            )

            show_selected = cur.fetchone()
            result = [dict(zip(Animes.fieldnames, show_selected))]

            # set_trace()

            conn.commit()
            cur.close()
            conn.close()

            return result

        except:
            raise NotFoundError

    @staticmethod
    def update(data, anime_id):

        Animes.create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute(
            """
                update animes set %s where id=%s returning *
            """,
            (data, anime_id,)
        )

        to_update = cur.fetchone()
        result = dict(zip(Animes.fieldnames, [elt for elt in to_update]))
        # set_trace()

        conn.commit()
        cur.close()
        conn.close()

        return result

    @staticmethod
    def delete(anime_id):

        Animes.create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute(
            """
                delete from animes where id=%s
            """,
            (anime_id,)
        )

        conn.commit()
        cur.close()
        conn.close()

        return ''
