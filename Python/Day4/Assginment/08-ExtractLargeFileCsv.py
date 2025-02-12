# import pandas as pd

# # Read the CSV file in chunks to handle large files
# chunk_size = 10000  # Adjust based on your system's memory
# total_sum, total_count = 0, 0

# for chunk in pd.read_csv('random.csv', chunksize=chunk_size):
#     total_sum += chunk['salary'].sum()  # Replace 'numeric_column' with your column name
#     total_count += len(chunk)

# # Calculate the average
# average = total_sum / total_count
# print(f"Average of numeric_column: {average}")

import pandas as pd

import time

def process_csv_data(filepath, chunksize=10000): # Added chunksize for large files

  """

  Reads a large CSV file in chunks and processes the data.

  Args:

    filepath: The path to the CSV file.

    chunksize: The number of rows to read and process at a time.

          Useful for handling files that don't fit in memory.

  Returns:

    None. Prints the processed data or performs other actions.

  """

  try:

    start_time_total = time.time() # Track total processing time

    # Use pandas read_csv with chunksize for memory efficiency

    for chunk in pd.read_csv(filepath, chunksize=chunksize, low_memory=False): # low_memory=False to prevent mixed dtypes

      start_time_chunk = time.time() # Track chunk processing time

      # Process the data chunk here. Examples:

      # 1. Print the first few rows of each chunk

      print(chunk.head())

      # 2. Perform calculations on columns

      if 'column_name' in chunk.columns: # Check if the column exists

        chunk['new_column'] = chunk['column_name'] * 2

      # 3. Filter rows based on conditions

      if 'another_column' in chunk.columns:

        filtered_chunk = chunk[chunk['another_column'] > 100]

      # 4. Aggregate data (example: calculate the mean of a column)

      if 'yet_another_column' in chunk.columns:

         mean_value = chunk['yet_another_column'].mean()

         print(f"Mean of yet_another_column in this chunk: {mean_value}")

      # ... Add your data processing logic here ...

      end_time_chunk = time.time()

      print(f"Time taken to process chunk: {end_time_chunk - start_time_chunk:.2f} seconds")

    end_time_total = time.time()

    print(f"Total time taken to process the CSV file: {end_time_total - start_time_total:.2f} seconds")

  except FileNotFoundError:

    print(f"Error: File '{filepath}' not found.")

  except pd.errors.EmptyDataError:

    print(f"Error: File '{filepath}' is empty.")

  except pd.errors.ParserError: # Handle CSV parsing errors

    print(f"Error: Could not parse CSV file '{filepath}'. Check the file format.")

  except Exception as e:

    print(f"An error occurred: {e}")

# Example usage:

file_path = "random.csv" # Replace with your CSV file path

process_csv_data(file_path, chunksize=50000) # Adjust chunksize as neede