from django.forms import ModelForm, Textarea

from .models import Task

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ["name", "description",]# "due_on"]
        labels = {
            "name": "Task",
            "description": "Description",
            #"due_on": "Due"
        }

        widgets = {"description": Textarea(attrs={"rows": 6})}