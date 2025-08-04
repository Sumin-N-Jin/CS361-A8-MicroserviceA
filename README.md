# Microservice A: Timezone Converter

The Microservice A I implemented in Sprint 2 converts UTC datetime strings to the local time based on a specified timezone offset and Daylight Saving Time (DST) status.

## Requesting Data

Use Python's `requests` module to send a `POST` request to the Flask REST API.

- **Endpoint**: `http://localhost:5001/convert`
- **Method**: POST
- **Content-Type**: `application/json`

### Required JSON payload fields:

- **command** (`str`): Must be `"convert_datetime"`
- **utc_datetime** (`str`): UTC datetime string in `"YYYY-MM-DD HH:MM"` format
- **timezone_offset** (`int`): Local timezone offset from UTC (range: -12 to +12)
- **is_dst** (`bool`): Whether DST is active (true/false)

### Example request:

data = {
    "command": "convert_datetime",
    "utc_datetime": "2025-08-01 13:00",
    "timezone_offset": -8,
    "is_dst": True
}

response = requests.post("http://localhost:5001/convert", json=data)
print(response.json())

### Example response:

{
  "date": "2025-08-01",
  "time": "06:00",
  "title": "CS361 Meeting",
  "location": "Online",
  "notes": "Discuss microservice integration",
  "uuid": "abc123"
}

### Receiving Data
Run the microservice using Flask:
python3 converter.py

This will start a local server at http://127.0.0.1:5001 listening for conversion requests.

### Server behavior:
Receives the POST request at /convert
Parses input and validates fields

Computes the converted datetime based on offset and DST

Returns a JSON response with the new datetime (converted_datetime)

Note: The server does not read or write any files. It only processes JSON requests and responses.

### File Handling
The main program (e.g., main.py) is responsible for:

Reading events from events.json

Sending datetime strings to the microservice for conversion

Writing converted events to converted_events.json

This ensures flexibility: the main program can freely determine input/output file names, and the microservice stays stateless and reusable.

### UML Sequence Diagram
This UML diagram shows how the main program interacts with the microservice via HTTP requests:

https://github.com/Sumin-N-Jin/CS361-A8-MicroserviceA/blob/main/CS361-A8-UML.jpeg

