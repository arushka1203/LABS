#TAsk1
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    print(response.content)

class ToDo:
    def __init__(self, todo_id, user_id, title, completed):
        self.todo_id = todo_id
        self.user_id = user_id
        self.title = title
        self.completed = completed

todo_item = ToDo(1, 1, "delectus aut autem", False)
new_todo = {
    "userId": todo_item.user_id,
    "title": todo_item.title,
    "completed": todo_item.completed
}

response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo)

if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    print(response.content)

todo_item.title = "new title"
todo_item.completed = True
modified_todo = {
    "userId": todo_item.user_id,
    "title": todo_item.title,
    "completed": todo_item.completed
}

response = requests.put(f'https://jsonplaceholder.typicode.com/todos/{todo_item.todo_id}', json=modified_todo)

if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    print(response.content)

#TASK2
import requests
import json
import random

def get_random_character():
    random_character_id = random.randint(1, 826)
    url = f"https://rickandmortyapi.com/api/character/{random_character_id}"
    response = requests.get(url)
    return response.json()

def output_character_info(character_info):
    print(json.dumps(character_info, indent=4))

def save_character_info_to_file(character_info, file_name):
    with open(file_name, "w") as file:
        json.dump(character_info, file, indent=4)

def get_episode_ids(character_info):
    episode_urls = character_info["episode"]
    episode_ids = [int(url.split("/")[-1]) for url in episode_urls]
    return episode_ids

def save_episode_urls_to_file(episode_ids, file_name):
    episode_urls = [f"https://rickandmortyapi.com/api/episode/{id}" for id in episode_ids]
    with open(file_name, "a") as file:
        for url in episode_urls:
            file.write(f"{url}\n")

class Episode:
    def __init__(self, episode_id, episode_name, episode_air_date, episode_code):
        self.id = episode_id
        self.name = episode_name
        self.air_date = episode_air_date
        self.code = episode_code

class Character:
    def __init__(self, character_id, character_name, character_status, character_species, character_type, character_gender):
        self.id = character_id
        self.name = character_name
        self.status = character_status
        self.species = character_species
        self.type = character_type
        self.gender = character_gender

random_character_info = get_random_character()
output_character_info(random_character_info)
save_character_info_to_file(random_character_info, "info_character_random.json")

episode_ids = get_episode_ids(random_character_info)
save_episode_urls_to_file(episode_ids, "all_episodes_with_character_random.txt")

episode_url = f"https://rickandmortyapi.com/api/episode/{episode_ids[0]}"
episode_response = requests.get(episode_url)
episode_data = episode_response.json()
episode = Episode(episode_data["id"], episode_data["name"], episode_data["air_date"], episode_data["episode"])

random_character = Character(random_character_info["id"], random_character_info["name"], random_character_info["status"], random_character_info["species"], random_character_info["type"], random_character_info["gender"])
print(random_character.name)
print(episode.name)
