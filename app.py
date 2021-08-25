"""Display the current date and time"""
from datetime import datetime
from datetime import date

TODAY = date.today().strftime("%B %d, %Y")
NOW = datetime.now().strftime("%H:%H:%S")
print(f"{TODAY} - {NOW}")
