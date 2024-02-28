from django import template
from menu_app.models import Menu


register = template.Library()

@register.inclusion_tag('main_menu.html', takes_context=True)
def draw_menu(context, name, menu_slug=None, menuitem_slug=None):
    '''
    This tag does four things
    1. Choise only root items of menu
    2. Check if the menu is active or not
    3. Get active slugs
    4. Give results in template
    '''
    menu_obj = {}
    menu = Menu.objects.filter(name=name).prefetch_related()
    active_menu = False
    active_slugs = []
    if menu:
        if menu[0].name not in menu_obj:
            menu_obj[menu[0].name] = []
        for item in menu[0].menuitem_set.all():
            if item.slug == menuitem_slug:
                ancestors = item.get_ancestors()
                [active_slugs.append(a.slug) for a in ancestors]
                active_slugs.append(menuitem_slug)
            if item.is_root():
                menu_obj[menu[0].name].append(item)
        if menu_slug == menu[0].slug:
            active_menu=True
    return {'menu': menu_obj, 'active_menu': active_menu, 'active_slugs': active_slugs, 'menuitem_slug': menuitem_slug}



