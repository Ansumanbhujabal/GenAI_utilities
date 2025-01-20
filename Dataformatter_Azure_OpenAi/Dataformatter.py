import os
import re
import json
import logging
import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Alignment, Font
from openai import AzureOpenAI

log_directory = '../Logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_directory, 'data_formatting.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
    api_version="2024-08-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# # Load the CSV file
# file_path = "discrepant_career_data_test - Sheet1.csv"
# df = pd.read_csv(file_path)

def fix_row_formatting(str):
    """
    Fixes formatting issues in a row by calling the GPT-4 API to rearrange misplaced column values.

    Args:
        row (pd.Series): A row from the DataFrame.

    Returns:
        dict: The corrected row as a dictionary, or the original row if an error occurs.
    """
    # row_dict = row.to_dict()

    # GPT-4 prompt
#     prompt = f"""
# The following row of data from a CSV file has formatting issues where column values are misplaced:
# {row_dict}
# Please rearrange the values to their correct columns based on these column definitions:
# 1. "Path 1" to "Path 4" should contain educational paths.
# 2. "Expected Earnings" should contain numeric or salary-related information.
# 3. "Skills" should contain relevant skill information.
# 4. Ensure all other columns are placed correctly as well.

# Return the corrected row as a JSON object.
# """
    prompt=f"""
# The following row of data  has formatting issues :
# {str}
1. Format the data in a better manner without changing the data and Make is SEO Friendly.
# Return the corrected data .

                                  """

    try:
        # Call GPT-4 API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data formatting assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )

        # Extract the GPT response content
        gpt_response = response.choices[0].message.content.strip()

        # Log GPT response
        logger.info(f"GPT Response: {gpt_response}")

        # Parse the GPT response as JSON
        corrected_row = json.loads(gpt_response)
        return corrected_row

    except json.JSONDecodeError as e:
        logger.error(f"JSON decoding error for row: {str}, GPT response: {gpt_response}, Error: {e}")
    except Exception as e:
        logger.error(f"Error processing row: {str}, Error: {e}")

    # Return the original row if any error occurs
    return str


# Apply the function to each row
logger.info("Starting to process rows for formatting corrections.")




ans=fix_row_formatting("Applicants must have&nbsp;passed a high schoolThe following curricular requirements are&nbsp;strongly recommended:Four years of EnglishThree years of mathematics (minimum course work equivalent to Algebra I, Geometry, Algebra II)Three years of science (two of which must be lab science)Two years of social scienceTwo years of language study other than English")
print("--------------------------------------------------->>>>>>>>>>>>>>>>>>>")
print(ans)
logger.info(ans)

# corrected_rows = []
# for index, row in df.iterrows():
#     corrected_row = fix_row_formatting(row)
#     corrected_rows.append(corrected_row)
#     logger.info(f"Processed row {index + 1}/{len(df)}")

# # Convert the corrected rows back to a DataFrame
# corrected_df = pd.DataFrame(corrected_rows)

# # Save the fixed file
# output_file = "fixed_csv_demo.csv"
# corrected_df.to_csv(output_file, index=False)

# logger.info(f"Corrected CSV saved to {output_file}")
# print(f"Corrected CSV saved to {output_file}")