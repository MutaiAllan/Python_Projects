from datetime import datetime

# Get the current date
current_date = datetime.now()

# Format the date with the month as words
formatted_date = current_date.strftime(" %B %d, %Y")

print("Current date with month as words:", formatted_date)