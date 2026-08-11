def bramha():
    nutrition = [
        {"name": "Apple", "calories": 130},
        {"name": "Avocado", "calories": 50},
        {"name": "Banana", "calories": 110},
        {"name": "Cantaloupe", "calories": 50},
        {"name": "Grapefruit", "calories": 60},
        {"name": "Honeydew Melon", "calories": 50},
        {"name": "Kiwifruit", "calories": 90},
        {"name": "Lemon", "calories": 15},
        {"name": "Orange", "calories": 80},
        {"name": "Grapes", "calories": 60},
        {"name": "Strawberry", "calories": 50}
    ]
    fruits = input("Fruit: ").title()
    for fruit in nutrition:
        if fruit["name"] == fruits:
            print(f"Calories: {fruit["calories"]}")
        
bramha()