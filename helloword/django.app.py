from django import models
class TodoItem(models.model):
    tite=
models.CharField(max_lenght=200)
     completed=
models.booleanField(default=False)
    def __str__(self):
        return self.title