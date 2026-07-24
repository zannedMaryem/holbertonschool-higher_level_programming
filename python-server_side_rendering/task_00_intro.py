import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template is not a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("attendees is not a list of dictionnairies")
        return
    if not template.strip():
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return
    
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
