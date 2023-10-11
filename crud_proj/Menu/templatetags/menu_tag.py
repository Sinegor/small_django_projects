# import typing
import re

# from typing import Union
from django import template
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch
from  Menu.models import Menu_model

register = template.Library()

def get_menu_data (context:RequestContext, menu_name:str, parent):        
        menu_items = Menu_model.objects.select_related().filter(category__name= menu_name)
        cur_path = context.request.path
        menu_list = []
        
        is_url = re.compile(r'^http[s]?://')
        for item in menu_items:
            item_path = item.url.strip()
            if re.match(is_url, item_path):
                url = item_path
            else:
                try:
                    url = reverse(item_path)
                except NoReverseMatch:
                    url = item_path    
            if url == cur_path:
                active_url = True
            else:
                active_url = False
            menu_list.append({
                'id': item.pk,
                'name': item.name,
                'link': url,
                'active': active_url,
                'parents':item.parents_id
            })
    
        return menu_list

@register.inclusion_tag('menu.html', takes_context=True,  )
def build_menu(context:RequestContext, menu_name = '', parent = None, cur_menu=''):
    result = {'menu_data':{}}
    current_menu =[]
    menu_list = []
    if parent !=None and 'menu_data' in context:
        result['menu_data'][cur_menu]={ 
                'menu_list':[],
                'current_menu': []
            }
        menu_list = context['menu_data'][cur_menu]['menu_list']
        current_menu = [item for item in menu_list if item['parents'] == parent]
        result['menu_data'][cur_menu]['menu_list'] =  menu_list
        result['menu_data'][cur_menu]['current_menu'] = current_menu

    else:
        if type(menu_name) == str:
            result['menu_data'][menu_name]={
                'menu_list':[],
                'current_menu': []
            }
            menu_list = get_menu_data(context, menu_name, parent)
            current_menu = [item for item in menu_list if item['parents'] == parent]
            result['menu_data'][menu_name]['menu_list'] =  menu_list
            result['menu_data'][menu_name]['current_menu'] = current_menu
        else:
            for item_menu in menu_name:
                result['menu_data'][item_menu]={
                'menu_list':'',
                'current_menu': ''
            }
                menu_list = get_menu_data(context, item_menu, parent)
                current_menu = [item for item in menu_list if item['parents'] == parent]
                result['menu_data'][item_menu]['menu_list'] = menu_list 
                result['menu_data'][item_menu]['current_menu'] =  current_menu
    return result
    