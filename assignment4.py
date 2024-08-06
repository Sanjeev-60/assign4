import csv

with open(r'F:\name.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

print(data)

with open(r'F:\new_schedule.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

def process_data(data, column_name):
    try:
        # Check if the column exists
        if column_name not in data[0]:
            raise KeyError(f"The column '{column_name}' does not exist in the data.")

        # Calculate the average
        values = [float(row[column_name]) for row in data]
        average = sum(values) / len(values)

        # Add the average column to each row
        for row in data:
            row['average'] = average

        return data
    except KeyError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: The column '{column_name}' contains non-numeric values.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None

def write_csv(file_path, data):
    try:
        with open('F:\name.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{file_path}'.")
    except csv.Error as e:
        print(f"Error: An error occurred while writing the CSV file: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

# Example usage
data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 35}]
processed_data = process_data(data, 'age')
if processed_data:
    write_csv('output.csv', processed_data)
