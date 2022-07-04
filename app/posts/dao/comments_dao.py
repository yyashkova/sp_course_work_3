import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def _load_comments(self):
        """
        Добавляем комментарии
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_comments_by_post_pk(self, post_pk):

        " Возвращает комментарии поста,ошибка значения если поста нет + пустой списокесли нет комментов вообще"
        comments = self._load_comments()
        comments_on_post = []
        for comment in comments:
            if comment["post_pk"] == post_pk:
                comments_on_post.append(comment)
        return comments_on_post
