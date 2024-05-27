#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge

    def teach(self, topic):
        pass
        if topic in self.knowledge:
            return f"{self.first_name} {self.last_name} is teaching {topic}."
        else:
            return f"{self.first_name} {self.last_name} does not know enough about {topic} to teach it."