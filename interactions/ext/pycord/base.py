import typing

from interactions import ext

authors: typing.List[ext.VersionAuthor] = [
    ext.VersionAuthor("fl0w", email="james.discord.interactions@gmail.com")
]

version = ext.Version(
    version="0.0.1",
    author=authors
)

base = ext.Base(
    name="interactions-pycord",
    version=version,
    link="https://github.com/interactions-py/pycord",
    description="An extension library for interactions.py to bridge with Pycord.",
    packages=["interactions.ext.pycord"],
    requirements=["discord-py-interactions>=4.2.0"]
)