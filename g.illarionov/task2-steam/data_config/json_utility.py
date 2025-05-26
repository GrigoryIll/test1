import json
import os


class JsonUtility:

    filepath = f"{os.path.dirname(os.path.abspath(__file__))}/data.json"

    def value_from_json(key_path, filepath=filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден: {filepath}")
            return None

        if isinstance(key_path, str):
            keys = key_path.split('.')
        else:
            print("Ошибка: key_path должен быть строкой.")
            return None

        current_value = data
        for key in keys:
            if key in current_value:
                current_value = current_value[key]
            else:
                print(f"Ключ '{key}' не найден в пути.")
                return None
        return current_value
