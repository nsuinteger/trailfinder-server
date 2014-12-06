from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render

# Create your views here.
from item.forms import ItemCreateForm
from item.models import Item
from jsonutil import json_success, json_fail


def item_list(request):
    item_list = Item.objects.all()

    if 'user_id' in request.GET:
        user_id = request.GET['user_id']
        item_list = Item.objects.filter(created_by=user_id)

    json_data = {}
    json_data['item_list'] = []
    for item in item_list:
        json_data['item_list'].append(
            item.to_string())
    return json_success(request, json_data)


def item_create(request):
    #todo: check permission
    try:
        form = ItemCreateForm(request.POST)
        if form.isValid():
            model_instance = form.save(commit=False)
            model_instance.create_by_id = request.user.id


    except KeyError:
        return json_fail("item create fail")



