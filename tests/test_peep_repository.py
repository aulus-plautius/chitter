from lib.peep_repository import PeepRepository
from lib.peep import Peep
from lib.user import User
from datetime import datetime


def convert_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")


def test_get_all_peeps(db_connection):
    db_connection.seed("seeds/peeps_users.sql")
    repo = PeepRepository(db_connection)
    peeps = repo.all()
    assert peeps == [
        Peep(
            1,
            "Just finished a great workout!",
            "John Doe",
            "@john_doe",
            convert_date("2024-08-22 08:00"),
        ),
        Peep(
            2,
            "Loving this sunny weather.",
            "Jane Smith",
            "@jane_smith",
            convert_date("2024-08-22 12:30"),
        ),
        Peep(
            3,
            "Reading a fantastic book right now.",
            "Mike Johnson",
            "@mike_j",
            convert_date("2024-08-21 19:00"),
        ),
        Peep(
            4,
            "Coffee always makes the day better.",
            "Emily Brown",
            "@emily_b",
            convert_date("2024-08-21 09:45"),
        ),
        Peep(
            5,
            "Excited for the weekend ahead.",
            "David Wilson",
            "@david_w",
            convert_date("2024-08-22 10:15"),
        ),
        Peep(
            6,
            "Had a great time exploring the city.",
            "Sarah Davis",
            "@sarah_d",
            convert_date("2024-08-22 16:00"),
        ),
        Peep(
            7,
            "Trying out a new recipe tonight.",
            "John Doe",
            "@john_doe",
            convert_date("2024-08-20 18:30"),
        ),
        Peep(
            8,
            "Just baked some fresh cookies.",
            "Sarah Davis",
            "@sarah_d",
            convert_date("2024-08-22 15:30"),
        ),
    ]


def test_create_new_peep(db_connection):
    db_connection.seed("seeds/peeps_users.sql")
    repo = PeepRepository(db_connection)
    peep = Peep(
        None,
        "this is a new peep",
        "Mike Johnson",
        "@mike_j",
        "2024-08-22 15:30",
        ["@jane_smith", "@sarah_d"],
    )
    repo.create(peep)
    peep = repo.find_with_users(9)
    print(peep.tagged_users)
    assert peep == Peep(
        9,
        "this is a new peep",
        "Mike Johnson",
        "@mike_j",
        convert_date("2024-08-22 15:30"),
        [
            User(2, "jane.smith@example.com", "Jane#4567", "Jane Smith", "@jane_smith"),
            User(4, "sarah.davis@example.com", "Sarah!8765", "Sarah Davis", "@sarah_d"),
        ],
    )


def test_find_with_users(db_connection):
    db_connection.seed("seeds/peeps_users.sql")
    repo = PeepRepository(db_connection)
    peep = repo.find_with_users(1)
    assert peep == Peep(
        1,
        "Just finished a great workout!",
        "John Doe",
        "@john_doe",
        convert_date("2024-08-22 08:00"),
        [
            User(3, "mike.johnson@example.com", "Mike@7890", "Mike Johnson", "@mike_j"),
            User(4, "sarah.davis@example.com", "Sarah!8765", "Sarah Davis", "@sarah_d"),
        ],
    )


def test_find_with_users_with_no_tags(db_connection):
    db_connection.seed("seeds/peeps_users.sql")
    repo = PeepRepository(db_connection)
    repo.create(
        Peep(None, "i have no friends", "any name", "@my_tag", "2024-08-30 08:00")
    )
    peep = repo.find_with_users(9)
    assert peep == Peep(
        9, "i have no friends", "any name", "@my_tag", convert_date("2024-08-30 08:00"), None
    )


def test_find_peep(db_connection):
    repo = PeepRepository(db_connection)
    peep = repo.find(1)
    assert peep == Peep(
        1,
        "Just finished a great workout!",
        "John Doe",
        "@john_doe",
        convert_date("2024-08-22 08:00"),
    )

def test_all_by_reverse_chronological_order(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    peeps = PeepRepository(db_connection)
    reverse_time = peeps.all_decending()
    assert reverse_time == [
        Peep(6, 'Had a great time exploring the city.', 'Sarah Davis', '@sarah_d', convert_date('2024-08-22 16:00')),
        Peep(8, 'Just baked some fresh cookies.', 'Sarah Davis', '@sarah_d', convert_date('2024-08-22 15:30')),
        Peep(2, 'Loving this sunny weather.', 'Jane Smith', '@jane_smith', convert_date('2024-08-22 12:30')),
        Peep(5, 'Excited for the weekend ahead.', 'David Wilson', '@david_w', convert_date('2024-08-22 10:15')),
        Peep(1, 'Just finished a great workout!', 'John Doe', '@john_doe', convert_date('2024-08-22 08:00')),
        Peep(3, 'Reading a fantastic book right now.', 'Mike Johnson', '@mike_j', convert_date('2024-08-21 19:00')),
        Peep(4, 'Coffee always makes the day better.', 'Emily Brown', '@emily_b', convert_date('2024-08-21 09:45')),
        Peep(7, 'Trying out a new recipe tonight.', 'John Doe', '@john_doe', convert_date('2024-08-20 18:30'))
    ]
def test_all_by_reverse_chronological_order_with_tags(db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    peeps = PeepRepository(db_connection)
    reverse_time = peeps.all_decending(with_tags=True)
    assert reverse_time[0] == Peep(6, 'Had a great time exploring the city.', 'Sarah Davis', '@sarah_d', convert_date('2024-08-22 16:00'), 
        [
            User(1, 'john.doe@example.com', 'Pass1234!', 'John Doe', '@john_doe'),
            User(3, 'mike.johnson@example.com', 'Mike@7890', 'Mike Johnson', '@mike_j')
        ]
    )


