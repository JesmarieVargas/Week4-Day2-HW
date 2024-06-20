# City Infrastructure Management System

# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner): # Method to change the vehicle's owner
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}")

# Creating instances
car = Vehicle("1HGBH41JXMN109186","Coupe", "Cora Martin")
truck = Vehicle("19XFA1F60BE043837", "F-350", "Rickey Spencer")

# Prints inital owners
print(f"The owner of vehicle {car.registration_number} is {car.owner}")
print(f"The owner of vehicle {truck.registration_number} is {truck.owner}")

# Updates initial owner name to new owner name
car.update_owner("Robin Justice")
truck.update_owner("Riley Gore")

# Prints new owners name with vehicle information
print(f"The new owner of vehicle {car.registration_number} is {car.owner}")
print(f"The new owner of vehicle {truck.registration_number} is {truck.owner}")

# Task 2: Event Management System Enhancement

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0

        def add_participant(self): # Method that increases the count of participants
             self.participant_count += 1

        def get_participant_count(self): # Method to retrieve the current count of participants
             return self.participant_count

# Creating an instance with the class Event

party = Event("Graduation", "2024-11-15")

party.add_participant() # Represent a participant
party.add_participant() # Represent a participant
party.add_participant() # Represent a participant

print(party.get_participant_count()) # Prints the count of the participants


             