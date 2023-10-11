import re

from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from ..models import TreeMenu

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):
    """
    Draw tree menu
    :param context:
    :type context: RequestContext
    :param name:
    :type name: str
    :param parent:
    :type parent: int
    :return:
    """

    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:

        is_url = re.compile(r'^http[s]?://')

        # Получаем урл, на который был направлен гет-запрос. Get path if request exist. ,
        #  а как он может не существовать, мы как на страницу попали?
        current_path = context['request'].path \
            if 'request' in context and isinstance(context['request'], HttpRequest) \
            else ''
# Из таблицы с пунктами меню мы получаем те, которые относятся к конкретному меню, имя которого передано в текущем html-файле
        data = TreeMenu.objects.select_related()\
            .filter(category__name=name)\
            .order_by('pk')

        menu = []

        for item in data:
# удаляем прбельные символы с конца и начала, типа на всякий случай, если в БД внесли лишний пробел:
            path = item.path.strip()

            target = '_self'
# проверяем, как у нас в БД записаны урлы (относительные или абсолютные):
            if is_url.match(path):
                url = path
                target = '_blank'
# если относительные пытаемся передать их как имя урл-шаблона в функцию и восстановить полные:
            else:
                try:
                    url = reverse(path)
                except NoReverseMatch:
                    url = path

            menu.append({
                'id': item.pk,
                'url': url,
# target в дальнейшем будут передан, как атрибут HTML, отвечающий за поведение ссылки:
                'target': target,
                'name': item.name,
                'parent': item.parent_id or 0,
# свойство, показывающее активная ссылка или нет:
                'active': True if url == current_path else False,
            })

    return {
        'menu': menu,
# первоначально создаётся и возвращается список корневых узлов (parent = 0), затем данный тег рекрусивно
# вызывается для каждого такого узла и в качестве parrent передаётся id этого узла, тем самым происходит поиск
# дочерних элементов
        'current_menu': [item for item in menu if item['parent'] == parent],
    }
