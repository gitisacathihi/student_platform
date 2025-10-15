from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    agree_terms = forms.BooleanField(
        label="I confirm my data is accurate and I agree to the terms.",
        required=True
    )

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'master_average', 'wilaya', 'agree_terms']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 16 or age > 30:
            raise forms.ValidationError("Age must be between 16 and 30.")
        return age

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Email must end with @gmail.com.")
        return email

    def clean_master_average(self):
        avg = self.cleaned_data['master_average']
        if avg < 0 or avg > 20:
            raise forms.ValidationError("Master average must be between 0 and 20.")
        return avg