from datetime import datetime

def convert_to_datetime(s, date_format):
    try:
        return datetime.strptime(s, date_format)
    except ValueError as e:
        print(f"Error parsing '{s}' with format '{date_format}': {e}")
        return None

# Example usage:
if __name__ == "__main__":
    try:
        date_string = "2023-06-30 12:00:00"
        date_format = "%Y-%m-%d %H:%M:%S"

        datetime_obj = convert_to_datetime(date_string, date_format)
        if datetime_obj is not None:
            print(f"Parsed '{date_string}' to datetime:", datetime_obj)
            print(f"Year: {datetime_obj.year}, Month: {datetime_obj.month}, Day: {datetime_obj.day}")

        invalid_date_string = "2023-06-30 12:00:00 PM"
        datetime_obj = convert_to_datetime(invalid_date_string, date_format)
        if datetime_obj is not None:
            print(f"Parsed '{invalid_date_string}' to datetime:", datetime_obj)

    except Exception as e:
        print(f"Error: {e}")
