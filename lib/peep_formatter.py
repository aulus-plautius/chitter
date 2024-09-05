from lib.peep import Peep
from datetime import datetime
class PeepFormatter:
    def __init__(self, peep: Peep) -> None:
        self.title = self.get_title(peep)
        self.body = peep.content
        self.tags = self.get_tags(peep)

    def get_title(self, peep: Peep):
        time = datetime.strftime(peep.time, "%-I:%M%p")
        date = datetime.strftime(peep.time, "%d/%m/%Y")
        return f"{time.lower()} {date}: {peep.handle} - {peep.name}"
    
    def get_tags(self, peep: Peep):
        if peep.tagged_users:
            return ", ".join([user.handle for user in peep.tagged_users])
        else:
            return None
    

    
