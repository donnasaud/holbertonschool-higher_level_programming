import os

def generate_invitations(template, attendees):
    # Type checks
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check for empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Iterate through attendees
    for index, person in enumerate(attendees, start=1):
        # Prepare data with "N/A" fallback
        name = person.get("name", "N/A") or "N/A"
        title = person.get("event_title", "N/A") or "N/A"
        date = person.get("event_date", "N/A") or "N/A"
        location = person.get("event_location", "N/A") or "N/A"

        # Replace placeholders
        filled = template.replace("{name}", name)\
                         .replace("{event_title}", title)\
                         .replace("{event_date}", date)\
                         .replace("{event_location}", location)

        # Write to file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(filled)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")

