# README.md

## 🎮 Дипломный проект: Образовательный курс по Python через создание игры

Этот проект представляет собой интерактивный курс по обучению Python через разработку пиксельной игры с использованием PyGame. Курс включает теоретические материалы, практические задания и готовую игровую платформу.

## 🛠 Технологический стек

- **Backend**: Django 3.2
- **Frontend**: HTML5, CSS3 (Grid/Flexbox), JavaScript
- **Игровой движок**: PyGame 2.1
- **База данных**: SQLite3
- **Стиль**: Пиксель-арт

## ⚙️ Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/ваш-username/дипломный-проект.git
cd дипломный-проект
```

### 2. Настройка виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
```

### 3. Установка зависимостей
Перед установкой убедитесь, что у вас установлен Python 3.8+.

```bash
pip install -r requirements.txt
```

Файл `requirements.txt` содержит:
```
Django==3.2.0
pygame==2.1.0
python-dotenv==0.19.0
Pillow==8.4.0
```

### 4. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта:

```ini
SECRET_KEY=ваш_секретный_ключ_для_django
DEBUG=True
```

**Важно!** Никогда не коммитьте `.env` в Git! Файл уже добавлен в `.gitignore`.

### 5. Применение миграций
```bash
python manage.py migrate
```

### 6. Запуск сервера
```bash
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000

## 🎮 Структура игрового проекта

Основные модули игры:
```
/game
  ├── main.py            # Главный игровой цикл
  ├── parent_class.py    # Базовый класс для игровых объектов
  ├── scenes/            # Кат-сцены игры
  ├── minigames/         # Мини-игры (Лабиринт, Птица, Гонки)
  ├── assets/            # Ресурсы (графика, звуки)
  └── game_rules.py      # Общие игровые правила
```

## 🌐 Особенности веб-платформы

### Модели данных
```python
class CoursePart(models.Model):
    title = models.CharField(max_length=100)

class Chapter(models.Model):
    part = models.ForeignKey(CoursePart, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class Course(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField()
    order = models.IntegerField()
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
```

### Запуск игры через веб-интерфейс
Игра интегрирована в Django через:
```python
# views.py
def launch_game(request):
    subprocess.Popen(['python', 'game/main.py'])
    return redirect('game_page')
```

## 🔒 Безопасность

1. Все секретные ключи хранятся в `.env`
2. Файл `.env` добавлен в `.gitignore`
3. Для production установите `DEBUG=False` в `.env`

## 📝 Лицензия

MIT License. Подробнее см. в файле LICENSE.

---

**Автор**: [Ваше имя]  
**Год**: 2023  
**Контакт**: ваш.email@example.com
