from django.contrib import admin
from .models import GameSession

admin.site.register(GameSession)
# class GameSessionAdmin(admin.ModelAdmin):
#     list_display = ('field1', 'field2', 'field3')  # replace with actual fields
#     search_fields = ('field1', 'field2')  # replace with actual fields
