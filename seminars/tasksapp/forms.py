from django import forms


class Game(forms.Form):
    choice_game = forms.ChoiceField(label="Выберите игру",
                                    choices=(('throws', 'Броски монеты'), ('bones', 'Игральные кости'), ('numbers', 'Случайное число')))
    attempts = forms.IntegerField(label="Количество попыток", min_value=1, max_value=64)
