from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Evaluators are expected to be admin to have had access to the Video Interviews
#Therefore, we select users from the database table who are admins as evaluators.
class Evaluator(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    candidate = models.CharField(max_length=100)
    scores = models.PositiveBigIntegerField() # to ensure only postive whole numbers can be scored.
    comment = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.candidate + ' - ' + self.scores