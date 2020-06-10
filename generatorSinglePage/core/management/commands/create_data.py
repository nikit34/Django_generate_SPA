import random, datetime, os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.images import ImageFile
from django.conf import settings

from ...models import Page, Category, Author


directory = os.path.join(settings.MEDIA_ROOT, 'test/doc')
names = os.listdir(directory)

categories = [
    'Instructions',
    'Scheme',
    'General Orders',
    'Local Decrees',
    'Reports'
]

authors = [
    'John','Petya','Liza',
    'Lena','Boris','Gena',
    'Masha','Kristina','Nikita',
    'Yegor','Denis','Ural',
    'Eduard','Natasha','Katya'
    'Michael','Luke','Sally',
    'Joe','Dude','Guy',
    'Barbara',
]

def generate_author_name():
    index = random.randint(0, 20)
    return authors[index]

def generate_category_name():
    index = random.randint(0, 4)
    return categories[index]

def generate_view_count():
    return random.randint(0, 100)

def generate_is_reviewed():
    return False if random.randint(0, 1) == 0 else True

def generate_publish_date():
    year = random.randint(2000, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The txt file that contains the pages name')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(os.path.join(settings.MEDIA_ROOT, f'test/{file_name}.txt'), 'w') as file:
            for row_name in names:
                name = row_name
                author_name = generate_author_name()
                category_name = generate_category_name()
                publish_date = generate_publish_date()
                views = generate_view_count()
                reviewed = generate_is_reviewed()

                author = Author.objects.get_or_create(
                    name=author_name
                )
                category = Category.objects.get_or_create(
                    name=category_name
                )
                page = Page(
                    name=name,
                    author=Author.objects.get(name=author_name),
                    category=Category.objects.get(name=category_name),
                    publish_date=publish_date,
                    views=views,
                    reviewed=reviewed
                )

                page.html_file.save(row_name, File(open(os.path.join(settings.MEDIA_ROOT, f'test/doc/{row_name}'), 'rb')))
                page.cover.save('test_img.png', ImageFile(open(os.path.join(settings.MEDIA_ROOT, 'test/test.png'), 'rb')))

                page.save()

                file.write(name + ',' + author_name + ',' + category_name + ',' + publish_date.strftime('%Y-%m-%d') + ',' + str(views) + ',' + str(reviewed) + '\n')
        file.close()
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))