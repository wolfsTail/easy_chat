from django import forms
from django.core.exceptions import ValidationError
from .models import User


class UserCreationForm(forms.ModelForm):
    """описание формы определяющей создание пользователя"""

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтори ввод пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "phone_number")

    def clean_password2(self):
        """метод определяет совпадение двух введённых паролей"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Введенные пароли не совпадают")
        return password2

    def save(self, commit=True):
        """метод сохраняет переданный пароль в виде его хэша"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
