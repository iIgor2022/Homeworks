import requests
import time


def get_questions(tag):
    current_time = int(time.time())
    previous_time = current_time - 172800
    url = f"https://api.stackexchange.com/2.3/questions"
    #https: // api.stackexchange.com / 2.3 / questions?fromdate = 1653696000 & todate = 1653868800 & order = desc & sort = activity & tagged = Python & site = stackoverflow
    params = {"fromdate": previous_time, "todate": current_time, "order": "desc", "sort": "activity", "tagged": tag, "site": "stackoverflow"}
    response = requests.get(url, params=params)
    print(f"Количество вопросов с тэгом {tag}: {len(response.json()['items'])}")
    for item in response.json()["items"]:
        print(f"Вопрос: {item['title']}")


if __name__ == "__main__":
    get_questions("Python")