import pytest


@pytest.fixture
def key_count_fixture():
    return {
        "foo": {"bar": {}},
        "baz": {
            "quux": {"corge": {"foo": {"corge": {}}}},
        },
        "quux": {},
        "corge": {},
    }


@pytest.fixture
def get_nth_fibonacci_sequence():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


@pytest.fixture
def filesystem_paths():
    paths = [
        "account/settings",
        "account/settings/activity/client/home",
        "profile/activity/team/client",
        "account/notifications",
        "about/contact/name",
        "about",
        "home",
        "about/team",
        "about/address",
    ]

    return {
        "string": "\n".join(paths),
        "hash": {
            "account": {
                "settings": {"activity": {"client": {"home": {}}}},
                "notifications": {},
            },
            "profile": {"activity": {"team": {"client": {}}}},
            "about": {
                "contact": {"name": {}},
                "team": {},
                "address": {},
            },
            "home": {},
        },
    }
