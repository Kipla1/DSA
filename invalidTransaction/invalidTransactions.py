def invalidTransactions(transactions):
    parsed = []
    for t in transactions:
        name, time, amount, city = t.split(',')
        parsed.append({
            'name': name,
            'time': int(time),
            'amount': int(amount),
            'city': city,
            'original': t
        })
    
    invalid = set()
    for i, current in enumerate(parsed):
        if current['amount'] > 1000:
            invalid.add(current['original'])
            continue
        for j, other in enumerate(parsed):
            if i == j:
                continue
            if (current['name'] == other['name'] and 
                current['city'] != other['city'] and 
                abs(current['time'] - other['time']) <= 60):
                invalid.add(current['original'])
                break
    return list(invalid)