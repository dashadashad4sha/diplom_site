from django.contrib import admin
from . import models

# admin.site.register(models.Course)
admin.site.register(models.Feedback)
admin.site.register(models.CoursePart)
admin.site.register(models.Type)
admin.site.register(models.Chapter)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['order', 'text', 'part_id', 'chapter_id', 'type_id']
    ordering = ['chapter_id', 'order']


admin.site.register(models.Course, CourseAdmin)
