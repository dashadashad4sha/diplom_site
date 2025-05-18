from .views import index, ChapterContentsView
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path(
        'course/<int:chapter_id>',
        ChapterContentsView.as_view(),
        name='chapter'
    ),
]
