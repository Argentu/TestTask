from django.db import models


class Menu(models.Model):
    ua_txt = models.CharField(max_length=15)
    en_txt = models.CharField(max_length=15)


class Sub_menu(models.Model):
    ua_txt = models.CharField(max_length=15)
    en_txt = models.CharField(max_length=15)
    value = models.CharField(max_length=200)
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Sub_sub_menu(models.Model):
    ua_txt = models.CharField(max_length=15)
    en_txt = models.CharField(max_length=15)
    value = models.CharField(max_length=200)
    parent = models.ForeignKey(Sub_menu, on_delete=models.CASCADE)