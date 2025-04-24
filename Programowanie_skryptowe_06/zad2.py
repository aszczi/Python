import datetime

# Słowniki z nazwami miesięcy i dni tygodnia
miesiace_pl = {
    1: 'styczeń', 2: 'luty', 3: 'marzec', 4: 'kwiecień', 5: 'maj', 6: 'czerwiec',
    7: 'lipiec', 8: 'sierpień', 9: 'wrzesień', 10: 'październik', 11: 'listopad', 12: 'grudzień'
}
dni_pl = {
    0: 'poniedziałek', 1: 'wtorek', 2: 'środa', 3: 'czwartek',
    4: 'piątek', 5: 'sobota', 6: 'niedziela'
}

# Aktualna data i czas
teraz = datetime.datetime.now()

# Nazwy po angielsku
miesiac_ang = teraz.strftime('%B')
dzien_tygodnia_ang = teraz.strftime('%A')

# Nazwy po polsku
miesiac_pl = miesiace_pl[teraz.month]
dzien_tygodnia_pl = dni_pl[teraz.weekday()]

# Format 12-godzinny z AM/PM
godzina_12h = teraz.strftime('%I:%M %p')

# Dzień roku
dzien_roku = teraz.timetuple().tm_yday

# Numer tygodnia roku
tydzien_roku = teraz.isocalendar()[1]

# Formatowanie daty
format_ddmmyyyy = teraz.strftime('%d/%m/%Y')
format_mmddyyyy = teraz.strftime('%m-%d-%Y')
format_yyyymmdd = teraz.strftime('%Y.%m.%d')

# Wyświetlenie danych
print(f"Miesiąc (angielski): {miesiac_ang}")
print(f"Miesiąc (polski): {miesiac_pl}")
print(f"Dzień tygodnia (angielski): {dzien_tygodnia_ang}")
print(f"Dzień tygodnia (polski): {dzien_tygodnia_pl}")
print(f"Godzina (12h z AM/PM): {godzina_12h}")
print(f"Dzień roku: {dzien_roku}")
print(f"Tydzień roku: {tydzien_roku}")
print(f"Format DD/MM/YYYY: {format_ddmmyyyy}")
print(f"Format MM-DD-YYYY: {format_mmddyyyy}")
print(f"Format YYYY.MM.DD: {format_yyyymmdd}")
