from django import forms
# import the class() stock from models
from .models import Stock

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock 
		fields = ["ticker"]