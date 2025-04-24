from datetime import datetime

# Napis wejściowy
data_string = "Jul 12 2022 4:45PM"

# Konwersja do datetime
data_datetime = datetime.strptime(data_string, "%b %d %Y %I:%M%p")

# Wyświetlenie rezultatu w żądanym formacie
print(data_datetime.strftime("%Y-%m-%d %H:%M:%S"))
