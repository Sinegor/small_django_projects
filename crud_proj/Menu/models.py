from django.db import models

class Menu_categories(models.Model):
    name = models.CharField(verbose_name= "Название меню", max_length=100)

class Menu_model(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=150, verbose_name='ссылка')
    category = models.ForeignKey(Menu_categories, on_delete=models.CASCADE, )
    parents = models.ForeignKey(
        'self', on_delete=models.CASCADE, 
         null=True, 
         blank=True, 
         default=0
         ) 




# class Menu_model (MPTTModel):
#     name = models.CharField(max_length=50, unique=True, verbose_name='Пункт меню')
#     url = models.URLField(blank=True, verbose_name="Ccskrf")
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родительский элемент')

#     class MPTTMeta:
#         verbose_name = "Меню"