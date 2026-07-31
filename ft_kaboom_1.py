def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    ingr = "THIS WILL RAISE AN UNCAUGHT EXCEPTION"
    print(f"Test import now - {ingr}")

    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record('Fantasy', ingr))


if __name__ == "__main__":
    main()
