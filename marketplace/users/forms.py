from django import forms
from django.utils import timezone
from .models import User  # Импортируйте вашу модель User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'birth_date', 'phone_number', 'city', 'total_spent', 'purchase_to_return_ratio']
        widgets = {
            'birth_date': forms.DateInput(
                format='%d-%m-%Y',  # Указываем формат даты для отображения
                attrs={
                    'class': 'form-control', 
                    'type': 'text',  # Используем текстовое поле, чтобы пользователь мог вводить дату
                    'placeholder': 'дд-мм-гггг'  # Подсказка для пользователя
                }
            ),
        }

    def clean_birth_date(self):
        date_input = self.cleaned_data.get('birth_date')
        try:
            # Преобразование строки в дату
            birth_date = timezone.datetime.strptime(date_input, '%d-%m-%Y').date()
            return birth_date
        except ValueError:
            raise forms.ValidationError("Неправильный формат даты. Используйте дд-мм-гггг.")