from __future__ import annotations

import json
import os
from typing import Dict, Union

import pydenticon

IdenticonType = Union[str, bytes]

STATE_FILEPATH = f"{os.getcwd()}/state/state.json"


class IdenticonService:

    def __init__(self, count=0, db = None):
        self._db: Dict[str, IdenticonType] = db or {}
        self._count = count
        self._generator = pydenticon.Generator(10, 10)

    def create_user_identicon(self, username: str) -> IdenticonType:
        if username in self._db:
            return self._db[username]
        identicon = self._generator.generate(str(self._count), 240, 240)
        self._count += 1
        self._db[username] = identicon
        return identicon

    def save(self):
        with open(STATE_FILEPATH, "w") as f:
            json.dump({
                "count": self._count,
                "db": json.dumps(self._db, default=str)
            }, f)

    @classmethod
    def load(cls) -> IdenticonService:
        try:
            with open(STATE_FILEPATH, "rb") as f:
                state = json.load(f)
                return cls(
                    count=state['count'],
                    db=json.loads(state['db']))
        except Exception:
            return cls()


    @staticmethod
    def write_identicon_to_file(username: str, identicon: IdenticonType, filepath='identicons') -> None:
        with open(f"{os.getcwd()}/{filepath}/{username}.png", "wb") as f:
            f.write(identicon)
