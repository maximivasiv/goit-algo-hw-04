def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat_info)
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line}")

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except OSError:
        print("Помилка при читанні файлу.")
        return []
