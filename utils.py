import json

def open_posts():
    """ Открывает json файл с данными """
    with open(data/'data.json') as file:
        data = json.load(file)
    return data


def get_posts_all():
    """ Возвращает посты """
    return open_posts()


def get_posts_by_user(user_name):
    """ Возвращает посты определенного пользователя,
    ошибка значения если пользователя нет + пустой список
    если нет постов вообще
    """
    pass


def get_comments_by_post_id(post_id):
    """ Возвращает комментарии поста,
    ошибка значения если поста нет + пустой список
    если нет комментов вообще
    """
    pass


def search_for_posts(query):
    """ Возвращает список постов по ключевому слову """
    pass


def get_posts_by_pk(pk):
    """ Возвращает один пост по его идентификатору """
    pass
