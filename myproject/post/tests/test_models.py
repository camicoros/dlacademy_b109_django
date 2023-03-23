import shutil
import tempfile
from io import BytesIO
from PIL import Image

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from post.models import Post


# добавить init
# уладить файл tests.py
# python manage.py test
# --verbosity 2 (0123) - уровень информирования
# python manage.py test myproject.YourTestClass.test_false_if_false


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('run one for all tests')

    def setUp(self):
        print('run for every test')

    def test_false_if_false(self):
        self.assertFalse(False)

    def test_false_if_true(self):
        self.assertTrue(False)

    def test_equal(self):
        self.assertEqual(1 + 1, 2)


MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PostModelTest(TestCase):
    @staticmethod
    def create_image(storage=None, filename="test.png", size=(100, 100), image_mode='RGB', image_format='PNG'):
        data = BytesIO()
        Image.new(image_mode, size).save(data, image_format)
        data.seek(0)
        if not storage:
            return data
        image_file = ContentFile(data.read())
        return storage.save(filename, image_file)

    @classmethod
    def setUpTestData(cls):
        author = get_user_model().objects.create(
            username="root", password="root"
        )
        file = cls.create_image(None, 'avatar.png')
        photo_file = SimpleUploadedFile('front.png', file.getvalue())
        Post.objects.create(
            author=author,
            image=photo_file,
            title="test post"
        )

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name

        self.assertEqual(field_label, 'title')

    def test_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/detail/1/')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()
