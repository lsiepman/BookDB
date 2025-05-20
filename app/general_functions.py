import json


def generate_db_string() -> str:
    # load credentials
    with open("credentials.json", "r", encoding="utf-8") as f:
        creds = json.load(f)

    db_creds = creds["database"]

    return (
        "mariadb+mariadbconnector://"
        f"{db_creds['user']}:{db_creds['password']}"
        f"@{db_creds['host']}:{db_creds['port']}/"
        f"{db_creds['default_database']}"
    )
