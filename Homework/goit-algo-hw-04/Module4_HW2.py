def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                cat_id, name, age = line.strip().split(',')
                
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
        return cats
    
    except FileNotFoundError:
        print("Файл не знайдено")
        return []

result = get_cats_info("/Users/markspc/Learning/03_Projects/IgorNemo-goit-algo-hw-04/GoIt_Python/Homework/goit-algo-hw-04/cats.txt")
print(result)
