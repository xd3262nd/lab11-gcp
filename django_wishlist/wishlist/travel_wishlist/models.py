from django.db import models
# Django User Models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

class Places(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True) # Dont require note
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def save(self, *args, **kwarg):
        # get reference to previous version of this Place
        old_place = Places.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            if old_place.photo != self.photo:
                self.delete_photo(old_place.photo)
        
        super().save(*args, **kwargs)

    def delete_photo(self, photo):
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    def delete(self, *args, **kwargs):
        if self.photo:
            self.delete_photo(self.photo)

        super().delete(*args, **kwargs)
        

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'No Photo'
        notes_str = self.notes[100:] if self.notes else 'No Notes'
        return f'{self.name}, visited? {self.visited} on {self.date_visited}. Notes: {notes_str}. Photo {photo_str}'