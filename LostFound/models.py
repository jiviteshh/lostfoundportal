from django.db import models

class FoundItem(models.Model):
    item_description = models.TextField(help_text="Describe the item (e.g., color, brand, size, unique features)")
    location_found = models.CharField(max_length=255, help_text="Where did you find the item?")
    date_found = models.DateField(help_text="Date when the item was found")
    upload_photo = models.ImageField(upload_to='found_items/', blank=True, null=True, help_text="Optional photo of the item")
    contact_info = models.CharField(max_length=255, blank=True, null=True, help_text="Contact email or phone number")

    def __str__(self):
        return f"Found Item: {self.item_description[:50]} - {self.location_found}"

class LostItem(models.Model):
    item_description = models.TextField()
    location_lost = models.CharField(max_length=255)
    date_lost = models.DateField()
    upload_photo = models.ImageField(upload_to='lost_items/', blank=True, null=True, help_text="Optional photo of the item")
    contact_info = models.CharField(max_length=255)
    date_reported = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.item_description} lost at {self.location_lost} on {self.date_lost}"
