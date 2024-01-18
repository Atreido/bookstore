from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,  blank=True, verbose_name="Ім'я")
    lastname = models.CharField(max_length=75, blank=True, verbose_name="Прізвище")
    bankCard = models.CharField(max_length=75, blank=True, verbose_name="Номер банківської картки")
    address = models.CharField(max_length=100, blank=True, verbose_name="Місто")
    city = models.CharField(max_length=75, blank=True, verbose_name="Місто")
    region = models.CharField(max_length=75, blank=True, verbose_name="Область")
    zip = models.CharField(max_length=10, blank=True, verbose_name="Поштовий Індекс")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    avatar = models.ImageField(upload_to='avatars', default="avatars/author-logo.png",  blank=True, verbose_name="Avatar")

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Деталі користувача"
        verbose_name_plural = "Деталі користувача"

class Categories(models.Model):
    category = models.CharField(max_length=20, unique=True, verbose_name="Категорія")
    def __str__(self):
        return self.category

    class Meta:     # создание перевода
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField()
    published_date = models.DateTimeField(auto_created=True, verbose_name="дата і час")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="користувач")
    image = models.ImageField(upload_to='uploads', blank=True)


    def __str__(self): # замена вывода на админке
        return self.title

    class Meta:     # создание перевода
        verbose_name = "Новина"
        verbose_name_plural = "Новини"


class Books(models.Model):
    title = models.CharField(max_length=75, verbose_name="Назва", unique=True)
    author = models.CharField(max_length=75, verbose_name="Автор")
    description = models.TextField(max_length=1000, verbose_name="Опис")
    additionalInfo = models.TextField(max_length=500, verbose_name="Додаткова інформація")
    image = models.ImageField(upload_to='uploads', verbose_name="Обкладинка")
    image2 = models.ImageField(upload_to='uploads', blank=True, verbose_name="Зображення 1")
    image3 = models.ImageField(upload_to='uploads', blank=True, verbose_name="Зображення 2")
    image4 = models.ImageField(upload_to='uploads', blank=True, verbose_name="Зображення 3")
    image5 = models.ImageField(upload_to='uploads', blank=True, verbose_name="Зображення 4")
    fk_category = models.ManyToManyField(Categories, blank=True, related_name="books")
    price = models.FloatField(verbose_name="Ціна")
    pages = models.SmallIntegerField(verbose_name="Сторінок")
    ISBN = models.CharField(max_length=25, verbose_name="ISBN")
    quantity = models.IntegerField(verbose_name="Кількість на складі")
    rating = models.CharField(max_length=50, verbose_name="Рейтинг")
    size = models.CharField(max_length=20, verbose_name="Розміри")

    def __str__(self): # замена вывода на админке
        return self.title
    class Meta:     # создание перевода
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Discount(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")
    description = models.TextField(max_length=300, verbose_name="Опис")
    discount = models.SmallIntegerField(default=0, verbose_name="Знижка")

    def __str__(self): # замена вывода на админке
        return self.name

    class Meta:     # создание перевода
        verbose_name = "Знижка"
        verbose_name_plural = "Знижки"


class Comments(models.Model):
    comment = models.TextField(verbose_name="Коментар")
    publish_date = models.DateTimeField(auto_created=True, verbose_name="Дата і час")
    posted = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Пост")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    name = models.CharField(max_length=50, verbose_name="Імя'")
    rating = models.CharField(max_length=50, verbose_name="Рейтинг")
    email = models.EmailField(verbose_name="Email")
    def __str__(self): # замена вывода на админке
        return f"{self.name} к посту '{self.posted.title}' написал: {self.comment[:10]}..."
    class Meta:     # создание перевода
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


class Orders(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Ім'я")
    lastname = models.CharField(max_length=75, verbose_name="Прізвище")
    bankCard = models.CharField(max_length=75, blank=True, verbose_name="Номер банківської картки")
    email = models.EmailField(max_length=75, verbose_name="email")
    address = models.CharField(max_length=100, verbose_name="Адреса")
    city = models.CharField(max_length=75, verbose_name="Місто")
    region = models.CharField(max_length=75, verbose_name="Область")
    zip = models.CharField(max_length=10, verbose_name="Поштовий Індекс")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    notes = models.TextField(blank=True, verbose_name="Коментар")
    orderedBook = models.ManyToManyField(Books, related_name="books")
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="користувач")

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
