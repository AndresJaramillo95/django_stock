from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
#functions!

# send request to pass in function and return something.
def home(request):
	import requests # grab something from  the internet
	import json 

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_cc50064356cf4c85aed9d7e6094025dd")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	#connect to API needs requests, and json
	import requests # grab something from  the internet
	import json 
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added"))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			# wrap the varible ticker_item in a str() because its calling a database object, not a string variable
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_cc50064356cf4c85aed9d7e6094025dd")
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':ticker})

def bucket(request):
	return render(request, 'bucket.html', {})





