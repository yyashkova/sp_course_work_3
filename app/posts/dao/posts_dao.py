import json


class PostsDAO:
    """ Класс ответственный за работу со всеми постами """

    def __init__(self, path):
        self.path = path

    def load_all_posts(self):
        """ Открывает json файл с данными """

        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """ Возвращает все посты """

        return self.load_all_posts()

    def get_posts_by_user(self, username):
        """ Возвращает посты определенного пользователя,
        ошибка значения если пользователя нет + пустой список
        если нет постов вообще
        """

        posts = self.get_posts_all()
        posts_by_user = []

        for post in posts:
            if post["poster_name"] == username:
                posts_by_user.append(post)

        return posts_by_user

    def search_for_posts(self, query):
        """ Возвращает список постов по ключевому слову query """

        posts = self.get_posts_all()
        posts_in_query = []

        for post in posts:
            if query.lower() in post["content"].lower():
                posts_in_query.append(post)

        return posts_in_query

    def get_posts_by_pk(self, pk):
        """ Возвращает один пост по его идентификатору """

        posts = self.get_posts_all()

        for post in posts:
            if post['pk'] == pk:
                return post
