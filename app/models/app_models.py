from dotenv import load_dotenv
from os import getenv
import psycopg2
from ipdb import set_trace

load_dotenv()

configs = {
    "host": getenv("HOST"),
    "database": getenv("DATABASE"),
    "user": getenv("USER"),
    "password": getenv("password")
}


class Animes:

    fieldnames = ['id', 'anime', 'released_date', 'seasons']

    def __init__(self, anime: str, released_date: str, seasons: int) -> None:
        self.anime = anime
        self.released_date = released_date
        self.seasons = seasons

    @staticmethod
    def create_table():
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute(
            """
                CREATE DATABASE IF NOT EXISTS animes(
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

    def get_create(self):
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute()

        conn.commit()

        cur.close()
        conn.close()

    @staticmethod
    def filter():
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update():
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete():
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        conn.commit()
        cur.close()
        conn.close()
