import argparse
from datetime import datetime, timezone
from enum import Enum

from jose import jwt


class Env(Enum):
    dev = "dev"

    def __str__(self):
        return self.value


def generate_token(secret: str, env: str) -> str:
    now = datetime.now(tz=timezone.utc)

    fields = {
        "exp": datetime(3000, 1, 1),
        "nbf": now,
        "iss": f"{env}",
        "aud": "client",
        "iat": now,
        "sub": f"client-{env}",
    }
    return jwt.encode(fields, secret, algorithm="HS256")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--secret", help="secret key for digital signature", type=str, required=True
    )
    parser.add_argument(
        "--env",
        help="environment: acs, dev, uat, or prod",
        type=Env,
        choices=list(Env),
        required=True,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    token = generate_token(args.secret, args.env)
    print(token)
