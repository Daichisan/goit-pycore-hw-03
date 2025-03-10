from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = given_date - current_date
        return delta.days
    
    except ValueError:
        return "Некоректний формат дати. Використовуйте формат 'YYYY-MM-DD'."

specific_date = "2023-03-23"
result_for_specific_date = get_days_from_today(specific_date)
print(result_for_specific_date)
