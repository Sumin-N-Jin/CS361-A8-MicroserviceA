import requests
import json
from datetime import datetime
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

print("Welcome to Event Planner App!")
print("This is your scheduling app that adjust times based on yout loca timezone.\n")

# Open JSON file
try:
    with open("events.json", "r") as f:
        events = json.load(f)
except FileNotFoundError:
    print(" events.json file not found. Please make sure the file exists.")
    exit()

# input offset timezone
while True:
    try:
        timezone_offset = int(input("Enter yout timezone offset (-12 to +12): ").strip())
        if -12 <= timezone_offset<= 12:
            break
        else:
            print("Must be between -12 and +12.")

    except ValueError:
        print("Invalid input. Please enter a number.")

is_dst_input = input("Is Daylight Saving Time (DST) active in your location? (y/n}: ").lower()
is_dst = is_dst_input.startswith("y")

# convert time
converted_events = []
print("\n Converting event times...\n")

for event in events:
    utc_input = f"{event['date']} {event['time']}"

    request_data = {
        "command": "convert_datetime",
        "utc_datetime": utc_input,
        "timezone_offset": timezone_offset,
        "is_dst": is_dst
    }

    try:
        response = requests.post("http://localhost:5001/convert", json=request_data)
        result = response.json()

        if "converted_datetime" not in result:
            print(f"Error converting event: {event.get('title', 'Untitled')}")
            print("Details:", result.get("error", "Unknown error"))
            continue

        dt = datetime.fromisoformat(result["converted_datetime"])
        event["date"] = dt.strftime("%Y-%m-%d")
        event["time"] = dt.strftime("%H:%M")

        converted_events.append(event)

    except Exception as e:
        print("Failed to connect to converter microservice.")
        print("Error:", str(e))
        exit()

with open("converted_events.json", "w") as f:
    json.dump(converted_events, f, indent=2)

print("All events converted successfully.")
print("Saved to: converted_events.json")
