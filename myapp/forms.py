from django.forms import Form,ModelForm
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        fields = {'name','amount','cetegory'}
