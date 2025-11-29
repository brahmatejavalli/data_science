
from django.db import models
class Prediction(models.Model):
    hours_studied = models.FloatField()
    attendance = models.FloatField()
    previous_score = models.FloatField()
    assignments_completed = models.IntegerField()
    predicted_pass = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Pass" if self.predicted_pass else "Fail"
