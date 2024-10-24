from django.contrib import admin
from .models import Students, Marks  # Import the models from your app's models.py

# Register the models to make them available in the Django admin
admin.site.register(Students)
admin.site.register(Marks)
