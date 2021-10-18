from Gym_Check_In.person import Person


class Gym:
    def __init__(self, gym_name, max_capacity):
        self.gym_name = gym_name
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
            return f"{self.gym_name} Gym is full at the moment. " \
                   f"Try checking in later."

        # Add person instance in the list.
        self.currently_in.append(person)

    @staticmethod
    def activate_membership(person: Person):
        if person.membership:
            return f"{person.name}'s membership is already active."

        person.membership = True
        return f"{person.name}'s membership is now active."

    def status(self):
        people_in = len(self.currently_in)
        average_age = sum([p.age for p in self.currently_in]) / people_in
        males = sum([1 for p in self.currently_in if p.gender == 'male'])
        females = sum([1 for p in self.currently_in if p.gender == 'female'])

        info = list()
        info.append(f"{self.gym_name}")
        info.append(f"People inside the gym: {people_in}/{self.max_capacity}")
        info.append(f"Their average age: {average_age}")
        info.append(f"Females: {females}")
        info.append(f"Males: {males}")

        return "\n".join(info)