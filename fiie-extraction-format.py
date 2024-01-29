{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3cfe74cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from datetime import datetime, timedelta\n",
    "import os\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ab639022",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openpyxl in d:\\anaconda\\lib\\site-packages (3.0.9)\n",
      "Requirement already satisfied: et-xmlfile in d:\\anaconda\\lib\\site-packages (from openpyxl) (1.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "571c1d7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the folder path containing the Excel files\n",
    "folder_path = \"C:\\\\Users\\\\vinay\\\\Desktop\\\\sowmya\\\\Data\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0fb797e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# List all Excel files in the folder\n",
    "data_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "065eb313",
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_monthly_filenames(start_date, end_date, file_extension):\n",
    "    filenames = []\n",
    "    current_date = start_date\n",
    "\n",
    "    while current_date <= end_date:\n",
    "        formatted_date = current_date.strftime(\"%b %Y\")\n",
    "        filenames.append(f\"{formatted_date}.{file_extension}\")\n",
    "        # Move to the next month\n",
    "        current_date = current_date + timedelta(days=32)\n",
    "        current_date = current_date.replace(day=1)\n",
    "\n",
    "    return filenames"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "65800fd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Jan 2022.xlsx', 'Feb 2022.xlsx', 'Mar 2022.xlsx', 'Apr 2022.xlsx', 'May 2022.xlsx', 'Aug 2022.xlsx', 'Aug 2023.xlsx', 'Jul 2023.xlsx', 'May 2023.xlsx', 'Jun 2023.xlsx', 'Sep 2022.xlsx', 'Oct 2022.xlsx', 'Nov 2022.xlsx', 'Dec 2022.xlsx', 'Jan 2023.xlsx']\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    # Define the date ranges\n",
    "    date_ranges = [\n",
    "        (datetime.strptime(\"01012022\", \"%d%m%Y\"), datetime.strptime(\"31052022\", \"%d%m%Y\")),\n",
    "        (datetime.strptime(\"01082022\", \"%d%m%Y\"), datetime.strptime(\"01082022\", \"%d%m%Y\")),\n",
    "        (datetime.strptime(\"August 2023\", \"%B %Y\"), datetime.strptime(\"August 2023\", \"%B %Y\")),\n",
    "        (datetime.strptime(\"july 2023\", \"%B %Y\"), datetime.strptime(\"july 2023\", \"%B %Y\")),\n",
    "        (datetime.strptime(\"May 2023\", \"%B %Y\"), datetime.strptime(\"June 2023\", \"%B %Y\")),\n",
    "        (datetime.strptime(\"Sep 2022\", \"%b %Y\"), datetime.strptime(\"Jan 2023\", \"%b %Y\"))\n",
    "    ]\n",
    "\n",
    "    # Initialize an empty list to store filenames\n",
    "    all_filenames = []\n",
    "\n",
    "    # Loop through each date range and generate filenames\n",
    "    for start_date, end_date in date_ranges:\n",
    "        filenames = generate_monthly_filenames(start_date, end_date, \"xlsx\")\n",
    "        all_filenames.extend(filenames)\n",
    "\n",
    "    # Print the combined list of filenames\n",
    "    print(all_filenames)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1ea3c38d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "all_filenames in list: ['Jan 2022.xlsx', 'Feb 2022.xlsx', 'Mar 2022.xlsx', 'Apr 2022.xlsx', 'May 2022.xlsx', 'Aug 2022.xlsx', 'Aug 2023.xlsx', 'Jul 2023.xlsx', 'May 2023.xlsx', 'Jun 2023.xlsx', 'Sep 2022.xlsx', 'Oct 2022.xlsx', 'Nov 2022.xlsx', 'Dec 2022.xlsx', 'Jan 2023.xlsx']\n",
      "Expected Filenames: ['Jan 2022.xlsx', 'Feb 2022.xlsx', 'Mar 2022.xlsx', 'Apr 2022.xlsx', 'May 2022.xlsx', 'Jun 2022.xlsx', 'Jul 2022.xlsx', 'Aug 2022.xlsx', 'Sep 2022.xlsx', 'Oct 2022.xlsx', 'Nov 2022.xlsx', 'Dec 2022.xlsx', 'Jan 2023.xlsx', 'Feb 2023.xlsx', 'Mar 2023.xlsx', 'Apr 2023.xlsx', 'May 2023.xlsx', 'Jun 2023.xlsx', 'Jul 2023.xlsx', 'Aug 2023.xlsx', 'Sep 2023.xlsx', 'Oct 2023.xlsx', 'Nov 2023.xlsx', 'Dec 2023.xlsx']\n"
     ]
    }
   ],
   "source": [
    "# Define the function to validate data received\n",
    "def validate_data_received(folder_path, start_date, end_date):\n",
    "    # Generate the list of expected filenames for the given date range\n",
    "    expected_filenames = generate_monthly_filenames(start_date, end_date, \"xlsx\")\n",
    "    \n",
    "    # Print all_filenames and expected_filenames for debugging\n",
    "    print(\"all_filenames in list:\", all_filenames)\n",
    "    print(\"Expected Filenames:\", expected_filenames)\n",
    "\n",
    "    # Create a list of dictionaries to store the validation results\n",
    "    validation_data = []\n",
    "\n",
    "    for expected_filename in expected_filenames:\n",
    "        if expected_filename.lower() in [file.lower() for file in all_filenames]:\n",
    "            status = \"Yes\"\n",
    "        else:\n",
    "            status = \"No\"\n",
    "        # Extract the month and year from the filename\n",
    "        month, year = expected_filename.split('.')[0].split()\n",
    "\n",
    "        validation_data.append({\"Month\": f\"{month} {year}\", \"Status\": status})\n",
    "\n",
    "    # Create a DataFrame from the validation data\n",
    "    validation_df = pd.DataFrame(validation_data)\n",
    "\n",
    "    # Save the validation results to an Excel file\n",
    "    validation_df.to_excel(\"data_validation3.xlsx\", index=False)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    start_date1 = datetime.strptime(\"01012022\", \"%d%m%Y\")\n",
    "    end_date1 = datetime.strptime(\"31122023\", \"%d%m%Y\")  # Assuming data for all of 2022 and 2023\n",
    "    validate_data_received(folder_path, start_date1, end_date1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}