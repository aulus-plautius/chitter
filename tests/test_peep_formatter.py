from lib.peep import Peep
from lib.peep_formatter import PeepFormatter
from datetime import datetime
from lib.user import User


def test_peep_gets_formatted():
    peep = Peep(
        6,
        "Had a great time exploring the city.",
        "Sarah Davis",
        "@sarah_d",
        datetime.strptime("2024-08-22 16:00", '%Y-%m-%d %H:%M'),
        [
            User(1, "john.doe@example.com", "Pass1234!", "John Doe", "@john_doe"),
            User(3, "mike.johnson@example.com", "Mike@7890", "Mike Johnson", "@mike_j"),
        ],
    )
    assert PeepFormatter(peep).title == "4:00pm 22/08/2024: @sarah_d - Sarah Davis"
    assert PeepFormatter(peep).body == "Had a great time exploring the city."
    assert PeepFormatter(peep).tags == "@john_doe, @mike_j"

def test_peep_gets_formatted_with_no_tags():
    peep = Peep(
        6,
        "Had a great time exploring the city.",
        "Sarah Davis",
        "@sarah_d",
        datetime.strptime("2024-08-22 16:00", '%Y-%m-%d %H:%M'),
        None
    )
    assert PeepFormatter(peep).title == "4:00pm 22/08/2024: @sarah_d - Sarah Davis"
    assert PeepFormatter(peep).body == "Had a great time exploring the city."
    assert PeepFormatter(peep).tags == None



