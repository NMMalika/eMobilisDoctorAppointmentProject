from django.contrib import admin
from .models import Doctor,Patient

admin.site.site_header = 'E_HEALTHCARE Administration'
admin.site.site_title = 'E_HEALTHCARE Admin'

class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["doctor_name" ,"registration_date","department","email"]
    search_fields = ["doctor_name" ,"registration_date","department","email"]
    list_per_page = 20
    inlines = [PatientInline]
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["appointment_number", "email","full_name"]
    search_fields = ["appointment_number", "email","full_name"]
    list_per_page = 20


admin.site.register(Doctor,DoctorAdmin)


