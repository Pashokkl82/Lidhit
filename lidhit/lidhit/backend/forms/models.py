import uuid
from django.db import models


class FormTemplate(models.Model):
    """
    Модель форма шаблона
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Наименовние формы',
                            blank=False)
    fname1 = models.CharField(max_length=255,
                            verbose_name='Поле email',
                            blank=False)
    fname2 = models.CharField(max_length=255,
                               verbose_name='Поле telephone',
                               blank=False)
    fname3 = models.CharField(max_length=255,
                               verbose_name='Поле data',
                               blank=False)
    fname4 = models.CharField(max_length=255,
                               verbose_name='Поле text',
                               blank=False)

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
        db_table = 'form_template'

    def __str__(self):
        return self.name
