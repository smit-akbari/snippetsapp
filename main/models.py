from django.db import models

class Snippetapp(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()  # Storing the actual code/text
    linenos = models.BooleanField(default=False)  # Boolean field for line numbers
    language = models.CharField(max_length=100)  # Language of the code snippet
    style = models.CharField(max_length=100) 

    def __str__(self):
        return self.title