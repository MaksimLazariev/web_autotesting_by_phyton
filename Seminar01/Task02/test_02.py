import pytest

from post_presence import take_data_list_of_posts, create_post


# тест по поиску поста '89681' по ключу 'id'
def test_01(take_token, sort_key, find_key):
    assert find_key in take_data_list_of_posts(take_token, sort_key)


# создаем пост с заданными title, description, content
# далее проверяем наличие поста по полю description
def test_02(take_token, title, description, content):
    create_post(take_token, title, description, content)
    assert description in take_data_list_of_posts(take_token, 'description',
                                                  'Me')


if __name__ == "__main__":
    pytest.main(['-vv'])
