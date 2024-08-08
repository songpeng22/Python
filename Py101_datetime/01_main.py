import random
from datetime import datetime, timedelta

def generate_random_date():
    start_date = datetime.now() - timedelta(days=5*365)  # 五年前
    end_date = datetime.now() + timedelta(days=5*365)    # 五年后
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%Y/%m/%d')

print(generate_random_date())