# snack_data.py

def get_snacks_by_mood_and_time(mood, time):
    snack_suggestions = {
        "happy": {
            "morning": ["Fruit salad", "Greek yogurt with honey"],
            "afternoon": ["Granola bar", "Apple slices with peanut butter"],
            "evening": ["Smoothie", "Popcorn"],
            "night": ["Dark chocolate", "Warm milk"]
        },
        "sad": {
            "morning": ["Oatmeal with banana", "Chia pudding"],
            "afternoon": ["Almonds", "Carrot sticks"],
            "evening": ["Soup", "Herbal tea"],
            "night": ["Chamomile tea", "Low-fat crackers"]
        },
        "tired": {
            "morning": ["Black coffee", "Boiled eggs"],
            "afternoon": ["Energy bar", "Fruit juice"],
            "evening": ["Protein shake", "Yogurt"],
            "night": ["Warm soup", "Banana"]
        }
    }
    return snack_suggestions.get(mood, {}).get(time, ["Try some fruits or nuts."])
