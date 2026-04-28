import re
import json

# Read receipt text
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Extract all prices
prices = re.findall(r'\d+\.\d{2}', text)

# Convert prices to float
prices_float = [float(p) for p in prices]

# Extract product names
products = re.findall(r'([A-Za-z\s]+)\s+\d+\.\d{2}', text)

products = [p.strip() for p in products]

# Calculate total amount
total = sum(prices_float)

# Extract date
date = re.search(r'\b\d{2}/\d{2}/\d{4}\b', text)

# Extract time
time = re.search(r'\b\d{2}:\d{2}\b', text)

# Find payment method
payment = re.search(r'(Cash|Card|Visa|MasterCard)', text, re.IGNORECASE)

result = {
    "products": products,
    "prices": prices_float,
    "total": total,
    "date": date.group() if date else None,
    "time": time.group() if time else None,
    "payment_method": payment.group() if payment else None
}

# Print formatted output
print(json.dumps(result, indent=4))