
# DL Academy
## Django project example

Тут будет размещаться код проекта с уроков.  
Каждый урок будет лежать в своей ветке.  
Актуальная версия в ветке master.  

### FAQ

<details><summary>Установка django в проект</summary>
<p>

```console
pip install django
```

если нужна определённая версия django

```console
pip install django==3.2.0
```

если хотим установить зависимости из файла requirements.txt

```console
pip install -r requirements.txt
```

если хотим создать файл requirements.txt и сохранить туда свои зависимости

```console
pip freeze > requirements.txt
```

</p>
</details>

<details><summary>Создание проекта</summary>
<p>

```console
django-admin startproject instagrammik
```

</p>
</details>

<details><summary>Создание приложения</summary>
<p>

```console
python manage.py startapp core
```

</p>
</details>

<details><summary>Запуск проекта</summary>
<p>

```console
python manage.py runserver
```

</p>
</details>

<details><summary>Установка pillow для работы с изображениями</summary>
<p>

```console
pip install pillow
```

</p>
</details>

<details><summary>Создание миграций</summary>
<p>

```console
python manage.py makemigrations
```

если вдруг django говорит что изменений нет, но вы уверены что есть  
можно попробовать указать приложение, где должны появиться миграции

```console
python manage.py makemigrations core
```

</p>
</details>

<details><summary>Применение миграций</summary>
<p>

```console
python manage.py migrate
```

можно применить миграции к конкретному приложению

```console
python manage.py migrate core
```

не удаляйте миграции вручную, если уже выполнили команду migrate вместе с ними!  
если сделали изменения в моделях, лучше сделайте ещё одну миграцию  

если вдруг вам очень надо удалить, то..  
миграции можно удалить только после их отмены в базе  
для этого нужно применить ту миграцию, которая была ещё норм  

```console
python manage.py migrate 0001
```

или отменить вообще все миграции в приложении

```console
python manage.py migrate core zero
```

</p>
</details>

<details><summary>Создание суперпользователя</summary>
<p>

```console
python manage.py createsuperuser
```

```console
Имя пользователя: root
Адрес электронной почты: 
Password: 
Password (again): 
Введённый пароль слишком похож на имя пользователя.
Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.
Введённый пароль слишком широко распространён.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

```

!!! не пугайтесь, если при вводе пароля символы в консоли не появляются  
так и задумано в целях "безопасности"))

если забыли пароль, но помните имя пользователя  
в консоли пароль можно поменять

```console
python manage.py changepassword имя_пользователя
```

</p>
</details>