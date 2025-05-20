import json
import os
import datetime
import random
import shutil

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# List of possible event names
event_names = [
    "Server started", "Configuration loaded", "User login", "User logout", 
    "Database query", "API request", "Cache miss", "Cache hit", 
    "File upload", "File download", "Payment processed", "Error occurred",
    "Backup completed", "Service restart", "Config update", "User registered",
    "Password reset", "Email sent", "Notification sent", "Report generated"
]

# Generate 50 random events
events = []
for i in range(1, 51):
    # Generate random timestamp within the last week
    days_ago = random.randint(0, 7)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)
    seconds_ago = random.randint(0, 59)
    
    event_time = datetime.datetime.now() - datetime.timedelta(
        days=days_ago, 
        hours=hours_ago,
        minutes=minutes_ago,
        seconds=seconds_ago
    )
    
    events.append({
        "id": i,
        "name": random.choice(event_names),
        "timestamp": event_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    })

# Sort events by timestamp (newest first)
events.sort(key=lambda x: x["timestamp"], reverse=True)

# Generate sample data
data = {
    "last_updated": datetime.datetime.now().isoformat(),
    "stats": {
        "users": 42,
        "events": 50,
        "average_response_time": 0.789
    },
    "events": events
}

# Path to the data file
data_file_path = "data/stats.json"
frontend_data_dir = "frontend/static/data"
frontend_data_file_path = f"{frontend_data_dir}/stats.json"

# Write data to JSON file
with open(data_file_path, "w") as f:
    json.dump(data, f, indent=2)

print("Data generated successfully!")

# Create frontend/static/data directory if it doesn't exist
try:
    os.makedirs(frontend_data_dir, exist_ok=True)
    
    # Copy the generated file to the frontend directory
    shutil.copy2(data_file_path, frontend_data_file_path)
    print(f"Data file successfully copied to {frontend_data_file_path}")
except Exception as e:
    print(f"Error copying data file to frontend directory: {e}")