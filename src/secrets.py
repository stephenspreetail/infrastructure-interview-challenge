from pprint import pprint
from _collections_abc import dict_items

SECRET_STORE = {
    "app1/production/AWS_ACCESS_KEY_ID": "PROD111111111EXAMPLE",
    "app1/production/AWS_SECRET_ACCESS_KEY": "production12345678",
    "app1/production/MY_SECRET": "production_secret_value",
    "app1/staging/AWS_ACCESS_KEY_ID": "STAGE22222222EXAMPLE",
    "app1/staging/AWS_SECRET_ACCESS_KEY": "staging12345678",
    "app1/staging/MY_SECRET": "staging_secret_value",
}


def list_secrets() -> dict_items:
    """
    Returns all secrets as a list of key/value pairs
    """
    return SECRET_STORE.items()


def print_secrets_store() -> None:
    """
    Prints the contents of the secret store
    """
    return pprint(SECRET_STORE)


def get_secret(key: str) -> str:
    """
    Returns the value of the secret stored under the given key
    """
    return SECRET_STORE[key]


def set_secret(key: str, value: str) -> None:
    """
    Sets the value of the secret stored under the given key. You may assume that this method also
    ensures that any applications using the secret instantly start using the new value.
    """
    SECRET_STORE[key] = value
