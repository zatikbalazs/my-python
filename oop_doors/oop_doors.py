# This is a small project for practicing OOP principles.

class Door:
    def __init__(self, width, height, material, status = "open"):
        self.width = width
        self.height = height
        self.material = material
        self.status = status

    def open(self):
        if self.status == "open":
            return "The door is already open."
        else:
            self.status = "open"

    def close(self):
        if self.status == "closed":
            return "The door is already closed."
        else:
            self.status = "closed"

class SafeDoor(Door):
    def __init__(self, width, height, locked = False):
        super().__init__(width, height, material = "steel")
        self.locked = locked

    def lock(self):
        if self.locked:
            return "It is already locked."
        else:
            self.locked = True

    def unlock(self):
        if not self.locked:
            return "It is already unlocked."
        else:
            self.locked = False
