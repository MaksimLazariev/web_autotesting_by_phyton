# Написать тест с использованием pytest и requests, в котором:
# ● Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# ● conftest.py содержит фикстуру авторизации по адресу
# https://test-stand.gb.ru/gateway/login с передачей параметров
# "username" и "password" и возвращающей токен авторизации
# ● Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого
# пользователя, для этого выполняется get запрос по адресу
# https://test-stand.gb.ru/api/posts c хедером, содержащим токен
# авторизации в параметре "X-Auth-Token". Для отображения
# постов другого пользователя передается "owner": "notMe".

import pprint

import requests
import yaml

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


def take_data_list_of_posts(token, key, owner="notMe"):
    # Получаем json по токену
    result_get = requests.get(url=data["get_url"],
                              headers={"X-Auth-Token": token},
                              params={"owner": owner})
    # Код ответа по запросу: result_get
    # json по запросу: result_get.json()
    # pprint.pprint(result_get.json())
    # Берем список словарей из json и добавляем все значения по ключу в список data_list
    post_list = result_get.json()['data']
    data_list = []
    for post_dict in post_list:
        data_list.append(str(post_dict[key]))
    return data_list


def create_post(token, title, description, content):
    requests.post(url=data["get_url"],
                  headers={"X-Auth-Token": token},
                  data={"title": title,
                        "description": description,
                        "content": content})


def take_token():
    result_post = requests.post(url=data["login_url"],
                                data={"username": data["login_site"],
                                      "password": data["password_site"]})
    return result_post.json()["token"]


if __name__ == "__main__":
    # create_post(take_token())
    pprint.pprint(take_data_list_of_posts(take_token(), 'description', 'Me'))
