def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    from .dark_validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    status = validation_result.split()[-1]
    if status == "VALID":
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell recorded: {spell_name} ({validation_result})"
