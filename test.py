import streamlit as st

# Define the number of columns you want
num_columns = 3

# Generate some content (e.g., numbers)
content = range(10)  # This could be any iterable you want to display

# Calculate how many items per column
items_per_column = len(content) // num_columns

# Create columns dynamically
for i in range(num_columns):
    start_index = i * items_per_column
    end_index = (i + 1) * items_per_column
    column_content = content[start_index:end_index]

    # Display content in each column
    st.write(f"Column {i + 1}")
    st.write(column_content)
