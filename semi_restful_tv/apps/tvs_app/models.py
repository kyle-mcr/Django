
from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["title"] = "Show name should be at least 5 characters"
        if len(postData['network']) < 5:
            errors["network"] = "Network name should be at least 5 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()
    def __repr__(self):
        return f"<Dojo object: {self.title} {self.network} {self.release} {self.description} {self.updated_at}>"


 #Validate the Add a TV Show form to ensure all fields are populated appropriately before adding to the database.
 #Display errors on the Add a TV Show form if the information is invalid.
 #Validate the Edit Show form with the same validations as creation.
 #Display errors on the Edit Show form if the information is invalid.
 #NINJA BONUS: Ensure the Release Date is in the past.
 #NINJA BONUS: Allow the description to be optional. If a description is provided, though, it should still be at least 10 characters.