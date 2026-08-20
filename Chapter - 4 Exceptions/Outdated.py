months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip()

        # Format: 9/8/1636
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        # Format: September 8, 1636
        else:
            month_name, rest = date.split(" ", 1)

            if month_name not in months or "," not in rest:
                continue

            day, year = rest.split(", ")

            month = months.index(month_name) + 1
            day = int(day)
            year = int(year)

        # Checking valid month and day
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    except (ValueError, AttributeError):
        pass