from django.contrib import admin
import services.models as models

admin.site.register(models.Category)
admin.site.register(models.Item)
admin.site.register(models.ReservedItemRequest)
admin.site.register(models.UserItemRequest)
admin.site.register(models.Tag)
