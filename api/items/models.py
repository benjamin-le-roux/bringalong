from django.db import models
from events.models import Event

class Item(models.Model):
    name = models.CharField(max_length=100)
    qty_needed = models.IntegerField(default=0, null=False)
    event = models.ForeignKey(Event, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Assignee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    event = models.ForeignKey(Event, related_name='assignee', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Bringing(models.Model):
    item = models.ForeignKey(Item, related_name="bringing_item", on_delete=models.CASCADE)
    assignee = models.ForeignKey(Assignee, related_name="bringing_assignee", on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    event = models.ForeignKey(Event, related_name='bringing', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} by {self.assignee.name} ({self.qty})"