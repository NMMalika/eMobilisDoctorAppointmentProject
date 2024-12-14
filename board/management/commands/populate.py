from django.core.management import BaseCommand

from board.models import Doctor


class Command(BaseCommand):
    def handle(self, *args, **options):

        doctors=[{"id":1,"doctor_name":"Shara Garm","kmpno":1670487371,"department":"Marketing","email":"sgarm0@e-recht24.de"},
{"id":2,"doctor_name":"Dyanne Booth","kmpno":296337552,"department":"Marketing","email":"dbooth1@ihg.com"},
{"id":3,"doctor_name":"Gwenette Vennard","kmpno":557439992,"department":"Product Management","email":"gvennard2@nationalgeographic.com"},
{"id":4,"doctor_name":"Schuyler Redolfi","kmpno":1145795222,"department":"Sales","email":"sredolfi3@foxnews.com"},
{"id":5,"doctor_name":"Dosi Kemmish","kmpno":2147405311,"department":"Product Management","email":"dkemmish4@cyberchimps.com"}]
        for doctor in doctors:
            doctor=Doctor(**doctor)
            doctor.save()
        self.stdout.write("Done")