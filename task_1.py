def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line}")

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)
    except OSError:
        print("Помилка при читанні файлу.")
        return (0, 0)
