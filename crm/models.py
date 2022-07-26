from django.db import models


# Create your models here.
# Таблица базы данных
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name="Название статуса")

    def __str__(self):
        """Возврат имен в админ панели"""
        return self.Status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    """Данные таблицы дата/имя/телефон/статус"""
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")
    """Несколько типов удаления:
          CASCADE  - при удалении родителя удаляютья потомки.
          SET_NULL - при удалении потомки переходят в состояние null.
          PROTECT  - запрещает удалять элементы полей."""
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Статус")

    def __str__(self):
        """Возврат имен в админ панели"""
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заявка")
    coment_text = models.TextField(verbose_name='Текст комментария')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        """Возврат имен в админ панели"""
        return self.coment_text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
