from typing import Optional

import typer

from identicon_service import IdenticonService

app = typer.Typer()


@app.command()
def create_identicon(username: str, filepath: Optional[str] = typer.Argument('identicons')):
    service = IdenticonService.load()
    identicon = service.create_user_identicon(username)
    service.write_identicon_to_file(username, identicon, filepath)
    service.save()


if __name__ == "__main__":
    app()