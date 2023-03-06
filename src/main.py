import typer

from identicon_service import IdenticonService


def main(username: str):
    service = IdenticonService()
    identicon = service.create_user_identicon(username)
    service.write_identicon_to_file(username, identicon)


if __name__ == "__main__":
    typer.run(main)