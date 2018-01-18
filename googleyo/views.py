from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.


def place_search(request):
	key = "AIzaSyDvhs0a2zmfD-G0OT7a23Q27vXhcaOsLUM"
	query = "Starbucks"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, query)

	next_page_token = request.GET.get('next_page')
	if next_page_token:
		url += "&pagetoken=%s"%(next_page_token)

	response = requests.get(url).json()

	context = {
	"response":response
	}

	#return render(request, 'place_search.html', context)
	return JsonResponse(response, safe=False)

def place_detail(request):
	key = "AIzaSyDvhs0a2zmfD-G0OT7a23Q27vXhcaOsLUM"
	place_id = request.GET.get('place_id')
	url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key, place_id)

	response = requests.get(url).json()

	context = {
	"place":response,
	}

	return render(request, 'place_detail.html', context)
	#return JsonResponse(response, safe=False)



