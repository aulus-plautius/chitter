from lib.peep import Peep
from datetime import datetime
def test_object_constructs():
    peep = Peep(1, 'Just finished a great workout!', 'John Doe', '@john_doe', datetime.strptime('2024-08-22 08:00', '%Y-%m-%d %H:%M'))
    assert peep.id == 1
    assert peep.content == 'Just finished a great workout!'
    assert peep.time == datetime.strptime('2024-08-22 08:00', '%Y-%m-%d %H:%M')
    assert peep.name == 'John Doe'
    assert peep.handle == '@john_doe'
    assert peep.tagged_users == None

def test_object_is_formatted_as_string():
    peep = Peep(1, 'Just finished a great workout!', 'John Doe', '@john_doe', datetime.strptime('2024-08-22 08:00', '%Y-%m-%d %H:%M'))
    assert str(peep) == 'Peep(1, Just finished a great workout!, John Doe, @john_doe, 2024-08-22 08:00)'

def test_two_objects_are_equal():
    peep1 = Peep(1, 'Just finished a great workout!', 'John Doe', '@john_doe', datetime.strptime('2024-08-22 08:00', '%Y-%m-%d %H:%M'))
    peep2 = Peep(1, 'Just finished a great workout!', 'John Doe', '@john_doe', datetime.strptime('2024-08-22 08:00', '%Y-%m-%d %H:%M'))
    assert peep1 == peep2

