class Gym:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.currently_in = {}

    def check_in(self, person):
        if person.active_membership:
            pass

        else:
            self.currently_in[person.name] = person

    def info(self):
        return len(self.currently_in)


#  membership
# benefits
# info
