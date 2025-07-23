from django.db import models
from django.urls import reverse

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=False)

    class Meta:
        ordering = ['id']
        verbose_name = "ToDo Item"

    def get_absolute_url(self):
        return reverse(
            'todo_list:detail',
                       kwargs={'pk': self.pk}
                       )
    def __str__(self) -> str:
        return f"{self.title}"


