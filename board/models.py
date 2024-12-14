from django.db import models


departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

# Create your models here.
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)
    kmp_no = models.IntegerField(unique=True)
    registration_date=models.DateTimeField("date registered")
    department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
    email = models.EmailField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        db_table='doctor'

class Patient(models.Model):
    doctor_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=30)
    registration_date=models.DateTimeField("date registered")
    waiting_status=models.BooleanField()

    @property
    def is_waiting(self):
      return bool(self.waiting_status)
