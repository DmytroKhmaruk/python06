
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ing_lower = ingredients.lower()
    for ingredient in allowed:
        if ingredient in ing_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
