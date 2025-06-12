# Q5: Invert the tab dictionary using a dictionary comprehension
tab = {
    'Montag': 'Monday',
    'Dienstag': 'Tuesday',
    'Mittwoch': 'Wednesday',
    'Donnerstag': 'Thursday',
    'Freitag': 'Friday',
    'Samstag': 'Saturday',
    'Sonntag': 'Sunday'
}

# Invert key and value
tab = {value: key for key, value in tab.items()}
print(tab)
