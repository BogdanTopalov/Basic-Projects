from Gym.person import Person


class Gym:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.currently_in = []

    def check_in(self, person: Person):

        # Check if person has active membership.
        if not person.membership:
            return f"{person.name}'s membership is not active. " \
                   f"Please active it before checking in."

        # Check if person has clean shoes.
        if not person.has_clean_shoes:
            return f"{person.name} doesn't have clean shoes. " \
                   f"In order to be checked in, {person.name} needs to have clean shoes."

        # Check if gym is full.
        if len(self.currently_in) >= self.max_capacity:
            return f"{self.name} Gym is full at the moment. " \
                   f"Try checking in later."

        # Add person instance in the list.
        self.currently_in.append(person)

    def info(self):
        return len(self.currently_in)


#  membership
# benefits
# info
