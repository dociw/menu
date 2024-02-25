from django.db import models
from treebeard.mp_tree import MP_Node


class Menu(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'

class MenuItem(MP_Node):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300)

    def menu_name(self):
        return self.menu.name

    def __str__(self):
        return self.name
