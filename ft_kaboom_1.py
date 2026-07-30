import alchemy.grimoire.dark_spellbook


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
ingr = "THIS WILL RAISE AN UNCAUGHT EXCEPTION"
print(f"Test import now - {ingr}")
print(f"Traceback (most recent call last): "
      f"{alchemy.grimoire.dark_spellbook.dark_spell_record('Fantasy', ingr)}")
print("")
