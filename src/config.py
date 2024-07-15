import tomllib as toml


from dataclasses import dataclass
from typing import Self, Iterable, Any
from os import environ


class Config:
    def __init__(self, config: dict):
        self.config = config

    def __repr__(self):
        return f"Config({self.config})"

    def __add__(self, other):
        if isinstance(other, Config):
            return self.config | other.config
        else:
            raise TypeError

    def add(self, path: str, item: None | str = None): ...


    @classmethod
    def from_path(cls, path: str, section: str | None = None):
        with open(path, 'rb') as file:
            config: dict = toml.load(file)

        config = get_env_variables(config)

        if section:
            config: dict = config[section]

        return cls(config)



# Utils
# Get a value from environ
# Example: $user => value [from environ]
def get_env_variables(config: dict[str, Any]) -> dict[str, Any]:
    new = dict()

    for key, item in config.items():
        if isinstance(item, dict):
            item = get_env_variables(item)

        elif isinstance(item, str) and len(item) > 1 and item[0] == "$":
            try:
                item = environ[item[1:]]
            except KeyError:
                raise KeyError(f"Didn't find a variable '{item[1:]}' in env")

        new[key] = item
    return new
