from django.db import models
from datetime import datetime
from django.urls import reverse

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Контент")
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    articleCover = models.CharField("Ссылка на изображение (1280x720)", max_length=500)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def get_absolute_url(self):
        return reverse("articleDetail", args=[self.pk])

    def __str__(self):
        return self.title

class Tour(models.Model):
    tourName = models.CharField("Наименование тура", max_length=255)
    description = models.TextField("Описание")
    price = models.FloatField("Цена тура", default=0.0)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    tourDateStart = models.DateField("Начало")
    tourDateEnd = models.DateField("Конец")
    tourCover = models.CharField("Ссылка на изображение (1280x720)", max_length=500)
    whatsapp = models.CharField("WhatsApp", max_length=500, null=True, blank=True)
    instagram = models.CharField("Instagram", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    def __str__(self):
        return self.tourName

    def get_absolute_url(self):
        return reverse("tourDetail", args=[self.pk])

class AboutPage(models.Model):
    title = models.CharField("Заголовок", max_length=255, null=True, blank=True)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Страница о приложении"
        verbose_name_plural = "Страница о приложении"

    def __str__(self):
        return self.title

class LoanItems(models.Model):
    placeName = models.CharField("Наименование места", max_length=255)
    smallDescription = models.TextField("Описание")
    whatsapp = models.CharField("WhatsApp", max_length=500, null=True, blank=True)
    instagram = models.CharField("Instagram", max_length=500, null=True, blank=True)
    map = models.CharField("Карта", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренда"

    def __str__(self):
        return self.placeName

class Camping(models.Model):
    campingName = models.CharField("Наименование тура", max_length=255)
    description = models.TextField("Описание")
    price = models.FloatField("Цена тура", default=0.0)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    tourDateStart = models.DateField("Начало")
    tourDateEnd = models.DateField("Конец")
    tourCover = models.CharField("Ссылка на изображение (1280x720)", max_length=500)
    whatsapp = models.CharField("WhatsApp", max_length=500, null=True, blank=True)
    instagram = models.CharField("Instagram", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Кемпинг"
        verbose_name_plural = "Кемпинг"

    def __str__(self):
        return self.campingName

    def get_absolute_url(self):
        return reverse("campingDetail", args=[self.pk])


class Museum(models.Model):
    museumName = models.CharField("Наименование музея", max_length=255)
    mapLink = models.CharField("Ссылка на карту", max_length=500)

    class Meta:
        verbose_name = "Музей"
        verbose_name_plural = "Музеи"

    def __str__(self):
        return self.museumName