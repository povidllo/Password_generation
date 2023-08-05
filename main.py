import secrets

def create_pas(len: int, characters: str) -> str:
    return "".join(secrets.choice(characters) for _ in range(len))
