from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import os
import urllib.request
import urllib.parse
from urllib.parse import urlencode
from app.settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = 1
    next_page_url = 'write your url'
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

