def is_leap(year):
    """Zwiera True, jeśli rok jest przestępny (reguły od 1582 r.)."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def run_tests():
    """Przeprowadza automatyczne testy, w tym dla lat przed kalendarzem gregoriańskim."""
    test_data = [
        (2000, True),  # podzielne przez 400 → przestępny
        (1900, False),  # podzielne przez 100, nie przez 400 → nieprzestępny
        (2024, True),  # podzielne przez 4 i nie przez 100 → przestępny
        (2023, False),  # niepodzielne przez 4
        (-4, True),  # ujemne lata – reguła działa tak samo
        (0, True),  # rok 0 matematycznie spełnia warunki
        (1500, True),  # przed kalendarzem gregoriańskim (1582 r.)
    ]

    for year, expected in test_data:
        result = is_leap(year)
        print(f"{'✓' if result == expected else '✗'}: {year} -> {result} (oczekiwanie: {expected})")


def main():
    run_tests()

    while True:
        try:
            year_input = input("Podaj rok: ").strip()
            year = int(year_input)
        except ValueError:
            print("Błąd: podano nieprawidłową wartość. Spróbuj ponownie.")
            continue

        # Walidacja zakresu – tylko lata od 1500 r. (przed wprowadzeniem kalendarza gregoriańskiego)
        if year < 1500 or year > 9999:
            print(f"Błąd: rok musi być w zakresie 1500–9999. Spróbuj ponownie.")
            continue

        if is_leap(year):
            print(f"{year} to rok przestępny!")
        else:
            print(f"{year} NIE jest rokiem przestępnym.")


if __name__ == "__main__":
    main()