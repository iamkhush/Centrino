from django.contrib import admin
from .models import dashboard, submitteddata, fleximodel

class DashboardAdmin(admin.ModelAdmin):
	pass

class SubmittedData(admin.ModelAdmin):
	pass

admin.site.register(submitteddata, SubmittedData)
admin.site.register(dashboard, DashboardAdmin)

admin.site.register(fleximodel)
