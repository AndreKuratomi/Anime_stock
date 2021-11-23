from ipdb import set_trace


class InvalidKeysError(Exception):
    def __init__(self, diff: str):
        self.diff = diff
        self.message = {
            "available keys": [
                "anime", "released_date", "seasons"],
            "wrong keys ended": f"{self.diff}"}

        super().__init__(self.message, self.diff)


class NotFoundError(Exception):
    def __init__(self):
        self.message = {"Error": "Not found!"}
        super().__init__(self.message)
