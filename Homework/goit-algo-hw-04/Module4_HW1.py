def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                # Розділяємо рядок по першій комі
                name, salary = line.strip().split(',', 1)
                total += int(salary)
                count += 1
        average = total / count if count > 0 else 0
        return (print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"))
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    
result = total_salary("/Users/markspc/Learning/03_Projects/IgorNemo-goit-algo-hw-04/GoIt_Python/Homework/goit-algo-hw-04/file.txt")
print(result)
