def suggest_outfits(weather_info, budget):
    outfits = {
        "cold": [
            {"image": "https://via.placeholder.com/200?text=Coat+%2B+Scarf", "description": "Warm coat with a cozy scarf"},
            {"image": "https://via.placeholder.com/200?text=Thermals+%2B+Boots", "description": "Thermals with winter boots"}
        ],
        "hot": [
            {"image": "https://via.placeholder.com/200?text=Cotton+Tee+%2B+Shorts", "description": "Light cotton tee and shorts"},
            {"image": "https://via.placeholder.com/200?text=Sun+Dress", "description": "Breezy sun dress"}
        ],
        "rainy": [
            {"image": "https://via.placeholder.com/200?text=Raincoat+%2B+Boots", "description": "Raincoat with waterproof boots"},
            {"image": "https://via.placeholder.com/200?text=Umbrella+%2B+Layers", "description": "Layers with a sturdy umbrella"}
        ],
        "moderate": [
            {"image": "https://via.placeholder.com/200?text=Jeans+%2B+Tee", "description": "Comfy jeans with a t-shirt"},
            {"image": "https://via.placeholder.com/200?text=Jacket+%2B+Sneakers", "description": "Light jacket with sneakers"}
        ]
    }

    if "cold" in weather_info:
        return outfits["cold"]
    elif "hot" in weather_info or "sunny" in weather_info:
        return outfits["hot"]
    elif "rain" in weather_info:
        return outfits["rainy"]
    else:
        return outfits["moderate"]
