import json

# 1️⃣ Python dictionary
data = {
    "name": "Alice",
    "age": 21,
    "is_student": True,
    "courses": ["Math", "Physics", "Programming"]
}

# 2️⃣ Convert Python to JSON string
json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)

# 3️⃣ Convert JSON string back to Python
parsed_data = json.loads(json_string)
print("Parsed name:", parsed_data["name"])

# 4️⃣ Write JSON to file
with open("sample-data.json", "w") as f:
    json.dump(data, f, indent=4)

# 5️⃣ Read JSON from file
with open("sample-data.json", "r") as f:
    loaded_data = json.load(f)
    print("Loaded data:", loaded_data)

# 6️⃣ Working with JSON array
json_array = '[{"id":1,"item":"apple"},{"id":2,"item":"banana"}]'
items = json.loads(json_array)
for item in items:
    print("Item:", item["item"])