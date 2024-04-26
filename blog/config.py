import tomllib as toml

from dataclasses import dataclass
from typing import Self, Iterable
from os import environ


class BaseConfig:
    @classmethod
    def from_path(cls, path: str, section: str | None = None):
        with open(path, 'rb') as file:
            config: dict = toml.load(file)

        config = get_env_variables(config)

        if section:
            config: dict = config[section]
    
        return cls(**config)
        

@dataclass
class ConfigDB(BaseConfig):
    name: str
    password: str
    host: str
    database: str


# Utils
# Get a value from environ
# Example: $user => value [from environ]
def get_env_variables(config: dict[str, any]) -> dict[str, any]:
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


if __name__ == "__main__":
    db1 = ConfigDB.from_path('config.toml', 'database')
    db2 = ConfigDB("he", 'STRAS', 'gsd', 'sadfw')

    print(db1, db2)


