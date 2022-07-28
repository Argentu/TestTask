from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *


class Menu_view(View):
    def get(self, request, *args, **kwargs):
        if kwargs.get('lang') == 'ua':
            data = []
            menu = Menu.objects.all()
            for list_item in menu:
                tmp={'txt': list_item.ua_txt}
                tmp['sub'] = []
                for sublist_item in list_item.sub_menu_set.all():
                    sub_menu = {'txt': sublist_item.ua_txt}

                    if sublist_item.value.startswith('s'):
                        sub_menu['sub'] = []
                        for sub_sub_list_item in sublist_item.sub_sub_menu_set.all():
                            sub_menu['sub'].append(
                                {
                                    'txt': sub_sub_list_item.ua_txt,
                                    'value': sub_sub_list_item.value
                                }
                            )

                    elif sublist_item.value.startswith('l'):    
                        sub_menu['value'] = sublist_item.value[2:]

                    tmp['sub'].append(sub_menu)

                data.append(tmp)

            return render(request, 'multi_level_menu/menu.html', {'flag': 'ua', 'data': data})

        elif kwargs.get('lang') == 'en':
            data = []
            menu = Menu.objects.all()
            for list_item in menu:
                tmp={'txt': list_item.en_txt}
                tmp['sub'] = []
                for sublist_item in list_item.sub_menu_set.all():
                    sub_menu = {'txt': sublist_item.en_txt}

                    if sublist_item.value.startswith('s'):
                        sub_menu['sub'] = []
                        for sub_sub_list_item in sublist_item.sub_sub_menu_set.all():
                            sub_menu['sub'].append(
                                {
                                    'txt': sub_sub_list_item.en_txt,
                                    'value': sub_sub_list_item.value
                                }
                            )

                    elif sublist_item.value.startswith('l'):    
                        sub_menu['value'] = sublist_item.value[2:]

                    tmp['sub'].append(sub_menu)

                data.append(tmp)

            return render(request, 'multi_level_menu/menu.html', {'flag': 'en', 'data': data})

        else: return redirect('/menu/ua')

def start(request):
    return redirect('/ua/')