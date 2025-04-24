from datetime import datetime, timedelta

dzisiaj = datetime.now()

data_minus_6 = dzisiaj - timedelta(days=6)
data_plus_6 = dzisiaj + timedelta(days=6)

print(f"Data 6 dni temu:   {data_minus_6.strftime('%Y-%m-%d')}")
print(f"Data dzisiejsza:   {dzisiaj.strftime('%Y-%m-%d')}")
print(f"Data za 6 dni:     {data_plus_6.strftime('%Y-%m-%d')}")