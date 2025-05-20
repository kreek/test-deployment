import json
import os
import datetime

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Generate sample data
data = {
    "last_updated": datetime.datetime.now().isoformat(),
    "stats": {
        "users": 42,
        "events": 123,
        "average_response_time": 0.789
    },
    "events": [
        {"id": 1, "name": "Server started", "timestamp": "2025-05-19T18:30:00Z"},
        {"id": 2, "name": "Configuration loaded", "timestamp": "2025-05-19T18:30:05Z"},
        {"id": 3, "name": "User login", "timestamp": "2025-05-19T19:45:12Z"}
    ]
}

# Write data to JSON file
with open("data/stats.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data generated successfully!")