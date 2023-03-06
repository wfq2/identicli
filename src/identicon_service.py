import os
from typing import Dict, Union

import pydenticon

IdenticonType = Union[str, bytes]


class IdenticonService:

    def __init__(self):
        self._db: Dict[str, IdenticonType] = {}
        self._count = 0
        self._generator = pydenticon.Generator(10, 10)

    def create_user_identicon(self, username: str) -> IdenticonType:
        if username in self._db:
            return self._db[username]
        identicon = self._generator.generate(str(self._count), 240, 240)
        self._count += 1
        self._db[username] = identicon
        return identicon

    @staticmethod
    def write_identicon_to_file(username: str, identicon: IdenticonType) -> None:
        with open(f"{os.getcwd()}/identicons/{username}.png", "wb") as f:
            f.write(identicon)
