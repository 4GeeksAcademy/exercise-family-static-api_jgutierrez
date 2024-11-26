
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1

        # Example list of members
        self._members = [
            {"id": self._generate_id(),
             "first_name": "John",
             "last_name": last_name,
             "age": 33,
             "lucky_numbers": [7,13,22]
            },

            {"id": self._generate_id(),
             "first_name": "Jane",
             "last_name": last_name,
             "age": 35,
             "lucky_numbers": [10,14,3]
            },

            {"id": self._generate_id(),
             "first_name": "Jimmy",
             "last_name": last_name,
             "age": 5,
             "lucky_numbers": [1]
             },
        ]


    # This method generates a unique 'id' when adding members into the list (you shouldn't touch this function)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return True

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        toDeleteMember = {}
        for member in self._members:
            if id == member["id"]:
                toDeleteMember = member
                self._members.remove(member)
                return  {"memberDeleted":toDeleteMember,"done": True}
        return None

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for member in self._members:
            if id == member["id"]:
                return member
        return None





    def get_all_members(self):
        return self._members


