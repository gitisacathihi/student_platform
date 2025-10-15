
from django.db import models

WILAYAS = [
    ('Adrar', 'Adrar'),
    ('Chlef', 'Chlef'),
    ('Laghouat', 'Laghouat'),
    ('Oum El Bouaghi', 'Oum El Bouaghi'),
    ('Batna', 'Batna'),
    ('Bejaia', 'Bejaia'),
    ('Biskra', 'Biskra'),
    ('Bechar', 'Bechar'),
    ('Blida', 'Blida'),
    ('Bouira', 'Bouira'),
    ('Tamanrasset', 'Tamanrasset'),
    ('Tebessa', 'Tebessa'),
    ('Tlemcen', 'Tlemcen'),
    ('Tiaret', 'Tiaret'),
    ('Tizi Ouzou', 'Tizi Ouzou'),
    ('Alger', 'Alger'),
    ('Djelfa', 'Djelfa'),
    ('Jijel', 'Jijel'),
    ('Setif', 'Setif'),
    ('Saida', 'Saida'),
    ('Skikda', 'Skikda'),
    ('Sidi Bel Abbes', 'Sidi Bel Abbes'),
    ('Annaba', 'Annaba'),
    ('Guelma', 'Guelma'),
    ('Constantine', 'Constantine'),
    ('Medea', 'Medea'),
    ('Mostaganem', 'Mostaganem'),
    ('MSila', 'M\'Sila'),
    ('Mascara', 'Mascara'),
    ('Ouargla', 'Ouargla'),
    ('Oran', 'Oran'),
    ('El Bayadh', 'El Bayadh'),
    ('Illizi', 'Illizi'),
    ('Bordj Bou Arreridj', 'Bordj Bou Arreridj'),
    ('Boumerdes', 'Boumerdes'),
    ('El Tarf', 'El Tarf'),
    ('Tindouf', 'Tindouf'),
    ('Tissemsilt', 'Tissemsilt'),
    ('El Oued', 'El Oued'),
    ('Khenchela', 'Khenchela'),
    ('Souk Ahras', 'Souk Ahras'),
    ('Tipaza', 'Tipaza'),
    ('Mila', 'Mila'),
    ('Ain Defla', 'Ain Defla'),
    ('Naama', 'Naama'),
    ('Ain Temouchent', 'Ain Temouchent'),
    ('Ghardaia', 'Ghardaia'),
    ('Relizane', 'Relizane'),
]

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    master_average = models.FloatField()
    wilaya = models.CharField(max_length=5   return f"{self.first_name} {self.last_name}".last_name}"
