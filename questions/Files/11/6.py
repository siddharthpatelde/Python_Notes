# Q6: Filter months with even values and convert to int
tab = {
    'Jan': '1', 'Feb': '2', 'Mär': '3', 'Apr': '4',
    'Mai': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
    'Sep': '9', 'Okt': '10', 'Nov': '11', 'Dez': '12'
}

# Keep only even-numbered months, convert value to int
filtered = {k: int(v) for k, v in tab.items() if int(v) % 2 == 0}
print(filtered)
