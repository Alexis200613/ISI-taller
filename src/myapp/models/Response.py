class Response:
    def __init__(self, body: str):
        self._body = body

    def get_body(self) -> str:
        return self._body