import requests

def get_dishes():
  
    url = "https://api-colombia.com/api/v1/TypicalDish"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        dishes = response.json()
        if isinstance(dishes, list):
            return dishes
        else:
            print("La API no devolvió datos válidos.")
            return []
    except requests.RequestException:
        print("No se pudo conectar a la API.")
        return []

def dish_fetch(dishes, num):
    """Obtiene el plato por número."""
    if num < 1 or num > len(dishes):
        return {"error": "Número de plato no válido."}
    return dishes[num - 1]

def main():
    dishes = get_dishes()
    if not dishes:
        print("No se pudo obtener platos desde la API. Intenta más tarde.")
        return

    print("¡Colombia con la mejor sazón!")
    
    while True:
        print("\nElige un plato por número o 0 para salir:")
        for i, d in enumerate(dishes, start=1):
            print(f"{i}. {d.get('name', 'Nombre no disponible')}")

        choice = input("Tu elección: ")
        if choice == "0":
            print("¡Hasta pronto!")
            break
        if not choice.isdigit():
            print("Por favor ingresa un número válido.")
            continue

        num = int(choice)
        dish = dish_fetch(dishes, num)
        if "error" in dish:
            print(dish["error"])
        else:
            print("\n--- Detalles del Plato ---")
            print("Nombre:", dish.get("name"))
            print("Descripción:", dish.get("description", "No disponible"))
            print("Ingredientes:", dish.get("ingredients", "No disponible"))
            print("Imagen (URL):", dish.get("imageUrl", "No disponible"))
            print("--------------------------")

if __name__ == "__main__":
    main()
    
