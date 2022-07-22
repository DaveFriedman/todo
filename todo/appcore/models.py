from django.db.models import *

from todo.users.models import User

class Task(Model):
    name = CharField(max_length=64)
    description = TextField(max_length=480)

    created_on = DateTimeField(auto_now_add=True)
    due_on = DateTimeField(null=True, blank=True)
    completed_on = DateTimeField(null=True, blank=True)
    is_completed = BooleanField(default=False)

    tasked_to = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.tasked_to}'s task: {self.name}"
