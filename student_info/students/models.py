
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


alpha_validator = RegexValidator(r'^[A-Za-z]+$', 'Only alphabetic characters are allowed.')


WILAYA_CHOICES = [
    ("Adrar","Adrar"),("Chlef","Chlef"),("Laghouat","Laghouat"),("Oum El Bouaghi","Oum El Bouaghi"),
    ("Batna","Batna"),("Bejaia","Bejaia"),("Biskra","Biskra"),("Bechar","Bechar"),
    ("Blida","Blida"),("Bouira","Bouira"),("Tamanrasset","Tamanrasset"),("Tebessa","Tebessa"),
    ("Tlemcen","Tlemcen"),("Tiaret","Tiaret"),("Tizi Ouzou","Tizi Ouzou"),("Algiers","Algiers"),
    ("Djelfa","Djelfa"),("Jijel","Jijel"),("Setif","Setif"),("Saida","Saida"),
    ("Skikda","Skikda"),("Sidi Bel Abbes","Sidi Bel Abbes"),("Annaba","Annaba"),("Guelma","Guelma"),
    ("Constantine","Constantine"),("Medea","Medea"),("Mostaganem","Mostaganem"),("M'Sila","M'Sila"),
    ("Mascara","Mascara"),("Ouargla","Ouargla"),("Oran","Oran"),("El Bayadh","El Bayadh"),
    ("Illizi","Illizi"),("Bordj Bou Arreridj","Bordj Bou Arreridj"),("Boumerdes","Boumerdes"),("El Tarf","El Tarf"),
    ("Tindouf","Tindouf"),("Tissemsilt","Tissemsilt"),("El Oued","El Oued"),("Khenchela","Khenchela"),
    ("Souk Ahras","Souk Ahras"),("Tipaza","Tipaza"),("Mila","Mila"),("Ain Defla","Ain Defla"),
    ("Naama","Naama"),("Ain Temouchent","Ain Temouchent"),("Ghardaia","Ghardaia"),("Relizane","Relizane"),
    ("Timimoun","Timimoun"),("Bordj Badji Mokhtar","Bordj Badji Mokhtar"),("Ouled Djellal","Ouled Djellal"),
    ("Beni Abbes","Beni Abbes"),("In Guezzam","In Guezzam"),("El Meghaier","El Meghaier"),("Meniaa","Meniaa")
]

class Student(models.Model):
    first_name = models.CharField(max_length=50, validators=[alpha_validator])
    last_name = models.CharField(max_length=50, validators=[alpha_validator])
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16), MaxValueValidator(30)])
    email = models.EmailField(unique=True)
    master_average = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(20)])
    wilaya = models.CharField(max_length=100, choices=WILAYA_CHOICES)
    agree_terms = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"