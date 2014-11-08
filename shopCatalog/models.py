# -*- coding: utf-8 -*-
# Create your models here.

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category)
    longName = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    imagePath = models.CharField(max_length=400)
    isAvailable = models.BooleanField()


class Like(models.Model):
    item = models.ForeignKey(Good)
    user = models.ForeignKey(User)


class Comment(models.Model):
    item = models.ForeignKey(Good)
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField()


# коммент отличается от ревью тем, что
# авторизированный пользователь может оставить еще и оценку к товару,
# что и будет считаться отзывом, а не комментом
class Review(Comment):
    rate = models.IntegerField()


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()

# храним скидку для данного города,
# что-то типа доп коэфициента
class City(models.Model):
    name = models.CharField(max_length=20)
    discount = models.FloatField()

# храним в бд, чтобы в случае выхода восстановить из бд
# будем хранить в случае незавершенного заказа
class Basket(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(Good)

# завершенные заказы
class Order(models.Model):
    user = models.ForeignKey(User)
    city = models.ForeignKey(City)
    items = models.ManyToManyField(Good)
    totalPrice = models.FloatField()

# акции к определенной категории товаров
class Action(models.Model):
    discount = models.FloatField()
    expireDate = models.DateField()
    category = models.ForeignKey(Category)

# баннеры на главной странице,
# возможно, их и не будет
class Banner(models.Model):
    imageUrl = models.CharField(max_length=400)
    displayStart = models.TimeField()
    displayEnd = models.TimeField()




