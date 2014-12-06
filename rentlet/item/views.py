from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render

# Create your views here.
from item.models import Item
from jsonutil import json_success


def item_list(request):
    item_list = Item.objects.all()
    json_data = {}
    json_data['item_list'] = []
    for item in item_list:
        json_data['item_list'].append({
            "item_name": "item1"
        })
    return json_success(request, json_data)
