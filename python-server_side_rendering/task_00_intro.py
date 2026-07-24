import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("template is not a string")
    if not isinstance(attendees, dict) or not all(isinstance(item, dict) for item in attendees):
        raise TypeError("attendees is not a list of dictionnairies")
    if not template.strip():
        raise ValueError("Template is empty, no output files generated")
    if not attendees:
        raise ValueError("No data provided, no output files generated")
    
    for idx, attendee in enumerate(attendees, start=1):
        # Fill placeholders, replacing missing values with "N/A"
        filled = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            filled = filled.replace("{" + key + "}", str(value))

        # --- Write to file ---
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(filled)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
