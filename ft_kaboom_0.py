import alchemy.grimoire


print("=== Kaboom 0 ===")
print("Using grimoire module directly")
ingr = "Earth, wind and fire"
print(f"Testing record light spell: "
      f"{alchemy.grimoire.light_spell_record('Fantasy', ingr)}")
print("")
