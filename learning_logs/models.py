from django.db import models

class Topic(models.Model):
    """Topic to be explored by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns text representation of the model"""
        return self.text

class Entry(models.Model):
    """Specific information on the progress of science"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns representation of a model in text string"""
        return f"{self.text[:50]}..."
