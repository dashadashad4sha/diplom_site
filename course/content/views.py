from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Course, Chapter


def index(request):
    return render(request, 'content/index.html')


class ChapterContentsView(ListView):
    model = Course
    template_name = 'content/course.html'
    context_object_name = 'contents'

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        self.chapter = get_object_or_404(Chapter, pk=chapter_id)
        v = Course.objects.filter(chapter_id=chapter_id)
        if v.count() != 0:
            self.part = v[0].part_id
        else:
            self.part = "Ошибка"
        return v

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapter'] = self.chapter
        context['part'] = self.part

        if self.part != "Ошибка":
            # Получаем все главы текущей части курса
            all_chapters = Chapter.objects.filter(
                course__part_id=self.part
            ).distinct()

            # Преобразуем в список ID глав для навигации
            chapter_ids = list(all_chapters.values_list('id', flat=True))
            for i in range(len(chapter_ids)):
                chapter_ids[i] -= 3

            # Определяем текущую позицию главы
            current_index = chapter_ids.index(self.chapter.id) if self.chapter.id in chapter_ids else 0

            context['all_chapters'] = all_chapters
            context['current_chapter_index'] = current_index
            context['total_chapters'] = len(chapter_ids)
        else:
            context['all_chapters'] = "Ошибка"
            context['current_chapter_index'] = "Ошибка"
            context['total_chapters'] = "Ошибка"

        return context
