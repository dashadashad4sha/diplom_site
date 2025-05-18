from django.db import models


class Course(models.Model):
    part_id = models.ForeignKey('CoursePart', on_delete=models.CASCADE, verbose_name="id части")
    chapter_id = models.ForeignKey('Chapter', on_delete=models.CASCADE, verbose_name="id главы")
    text = models.TextField('Текст')
    type_id = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name="id типа текста")
    order = models.IntegerField(verbose_name="Порядковый номер внутри главы")

    def __str__(self):
        return f'{self.order} {self.text[:10]}'


class Feedback(models.Model):
    title = models.CharField('Заголовок отзыва', max_length=100)
    text = models.TextField('Текст отзыва')

    def __str__(self):
        return self.title


class CoursePart(models.Model):
    part_title = models.CharField('Название части курса', max_length=100)

    def __str__(self):
        return self.part_title


class Type(models.Model):
    type_title = models.CharField('Название типа текста', max_length=100)

    def __str__(self):
        return self.type_title


class Chapter(models.Model):
    chapter_title = models.CharField('Название главы', max_length=100)

    def __str__(self):
        return str(self.chapter_title)

