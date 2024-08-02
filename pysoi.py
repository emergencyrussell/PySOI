import os
import random
import pandas as pd
import xlsxwriter

# Step 1: Load word lists
def load_word_lists(directory):
    word_lists = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                word_lists[filename] = [line.strip() for line in file.readlines()]
    return word_lists

# Step 2: Assign words to sections
def assign_words(word_lists, sections, heading_word_list):
    assignments = {}
    remaining_lists = list(word_lists.keys())
    remaining_lists.remove(heading_word_list)  # Remove the heading word list from remaining lists

    for section in sections:
        valid_list_found = False
        while remaining_lists and not valid_list_found:
            word_list_file = random.choice(remaining_lists)
            word_list = word_lists[word_list_file]
            if len(word_list) >= len(sections[section]):
                valid_list_found = True
            else:
                remaining_lists.remove(word_list_file)

        if not valid_list_found:
            raise ValueError(f"No word list has enough words for section '{section}'. Please ensure the word lists are sufficient and try again.")

        assignments[section] = dict(zip(sections[section], random.sample(word_list, len(sections[section]))))

    return assignments

# Step 3: Create Excel file with formatted sections and auto-adjusted column width
def create_excel(assignments, heading_words, sarneg_word, output_filename, sections_with_headings, word_lists):
    with pd.ExcelWriter(output_filename, engine='xlsxwriter') as writer:
        workbook = writer.book
        worksheet = workbook.add_worksheet('Assignments')

        pastel_colors = {
            'Orders/Status': '#FFB6C1',  # Light Pink
            'SITREP': '#ADD8E6',  # Light Blue
            'RESOURCE': '#90EE90',  # Light Green
            'Position': '#FFDAB9',  # Peach Puff
            'Location': '#FFD8FF', 
            'AuthSection1': '#F0E68C',  # Khaki
            'AuthSection2': '#D3D3D3',  # Light Gray
            'AuthSection3': '#E6E6FA',  # Lavender
        }

        col_width = 2  # Width of each section in columns
        max_cols = 6  # Maximum number of columns before wrapping
        max_rows = 12  # Maximum rows before wrapping
        odd_col_width = 13
        even_col_width = 16
        current_row = 0
        current_col = 0
        total_columns_used = 0  # Track total columns used

        for section, options in assignments.items():
            section_color = pastel_colors.get(section, '#FFFFFF')
            section_col_span = ((len(options) - 1) // max_rows + 1) * col_width  # Calculate the correct span
            
            if sections_with_headings.get(section, False):
                heading_word = random.choice(heading_words)
                section_header = f"{section} \"{heading_word}\""
            else:
                section_header = section
            
            header_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': section_color, 'border': 2, 'font_size': 13})
            cell_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bg_color': section_color, 'right': 2, 'bottom': 1, 'font_size': 11})
            bold_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': section_color, 'left': 2, 'bottom': 1, 'font_size': 11})

            worksheet.merge_range(current_row, current_col, current_row, current_col + section_col_span - 1, section_header, header_format)
            row_offset = 1

            for i, (option, word) in enumerate(options.items()):
                row = current_row + row_offset + (i % max_rows)
                col = current_col + (i // max_rows) * col_width

                worksheet.write(row, col, option, bold_format)
                worksheet.write(row, col + 1, word, cell_format)

                if (i + 1) % max_rows == 0:
                    col += col_width

            current_col += section_col_span
            total_columns_used = max(total_columns_used, current_col)
            if current_col >= max_cols:
                current_col = 0
                current_row += max_rows + 1

        # Set the column widths for all columns uniformly
        for col in range(total_columns_used):
            width = odd_col_width if col % 2 == 0 else even_col_width
            worksheet.set_column(col, col, width)

        # Add the authentication table
        sarneg_format = workbook.add_format({'bold': True, 'font_name': 'Courier New', 'align': 'left', 'valign': 'vcenter', 'font_size': 15})
        auth_num_format = workbook.add_format({'bold': True, 'font_name': 'Courier New', 'align': 'left', 'valign': 'vcenter'})
        header_format = workbook.add_format({'bold': True, 'font_name': 'Courier New', 'align': 'left', 'valign': 'vcenter', 'font_size': 15})

        current_row += 1 # Move down after the sections
        worksheet.write(current_row, 0, "AUTHENTICATION TABLE", header_format)
        current_row += 1
        spaced_sarneg_word = ' '.join(sarneg_word)  # Add spaces between each letter
        worksheet.write(current_row, 0, spaced_sarneg_word, sarneg_format)
        worksheet.write(current_row + 1, 0, ' '.join(str(i) for i in range(10)), sarneg_format)

        # Prepare unique word lists for each Auth Section
        auth_word_lists = {}
        remaining_lists = list(word_lists.keys())
        for auth_section in ['AuthSection1', 'AuthSection2', 'AuthSection3']:
            valid_list_found = False
            while remaining_lists and not valid_list_found:
                word_list_file = random.choice(remaining_lists)
                word_list = word_lists[word_list_file]
                if len(word_list) >= 4:  # Each Auth Section needs at least 4 words
                    valid_list_found = True
                    auth_word_lists[auth_section] = word_list
                    remaining_lists.remove(word_list_file)
                else:
                    remaining_lists.remove(word_list_file)

            if not valid_list_found:
                raise ValueError(f"Not enough unique word lists for Auth Section '{auth_section}'. Please ensure the word lists are sufficient and try again.")

        # Add Auth Sections
        auth_sections = {
            'AuthSection1': ['Affirmative/Yes', 'Negative/No', 'Unknown', 'Emergency'],
            'AuthSection2': ['Interrogative', 'ALT FREQ', 'ALT SOI', ' '],
            'AuthSection3': ['Challenge', 'Password', 'Running Password', 'Number Combo']
        }

        auth_start_row = current_row + 3  # Start Auth Sections after the Sarneg section
        current_col = 0  # Reset to the start column for Auth Sections

        for auth_section, options in auth_sections.items():
            auth_color = pastel_colors.get(auth_section, '#FFFFFF')
            auth_col_span = ((len(options) - 1) // 4 + 1) * col_width  # Calculate the correct span for Auth Sections
            auth_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': auth_color, 'right': 2, 'bottom': 1, 'font_size': 11})

            current_auth_col = current_col  # Start at Column A for Auth Sections

            for i, option in enumerate(options):
                row = auth_start_row + (i % 4)
                col = current_auth_col + (i // 4) * col_width

                if option == 'Number Combo':  # Last option in AuthSection3
                    number_combination = random.choice([n for n in range(3, 16, 2)])
                    worksheet.write(row, col, option, auth_format)
                    worksheet.write(row, col + 1, number_combination, auth_format)
                else:
                    word_list = auth_word_lists[auth_section]
                    random_word = random.choice(word_list)
                    word_list.remove(random_word)  # Ensure the word does not repeat
                    worksheet.write(row, col, option, auth_format)
                    worksheet.write(row, col + 1, random_word, auth_format)

            current_col += auth_col_span
            if current_col >= max_cols:
                current_col = 0
                auth_start_row += 5  # Leave space after Auth Sections

        writer._save()

# Define sections and their options
sections = {
    'Orders/Status': ["Move", "Halt/Pause", "Continue", "Expedite", "Delay", "Cease/Stop", "Until/NLT", "I Request", "Meter", "Mile", "Hour", "Day", "Attack", "Defend", "Guard", "Recon", "Hide", "Rendezvous", "Return", "Rest", "Withdraw", "Destroy"],
    'SITREP': ["Green", "Yellow", "Red", "Black", "LACE", "SALUTE", "Status", "Enemy", "Friendly", "Civilian", "Local Law", "EPW"],
    'RESOURCE': ["Water", "Ammo", "Casualties", "Equipment", "Battery", "Medical", "Intelligence", "Comms", "Reinforcemnts", "Time", "Small Arms", "Hvy Weaps"],
    'Position': ["Forward", "Backward", "Left", "Right", "High", "Low", "North", "South", "East", "West", "Clockwise", "Counterclockwise"],
    'Location': ["In/At/On", "Zone/Area", "Route", "OBJ", "RP", "AA", "FLOT", "FEBA", "LOA", "TRP", "Danger Area"],


}

# Define which sections should have random heading words
sections_with_headings = {
    'Orders/Status': False,
    'SITREP': True,
    'RESOURCE': False,
    'Position': False,
    'Location': True,
}

# Directory containing word list .txt files
word_list_directory = 'soi-lists'

# Load word lists
word_lists = load_word_lists(word_list_directory)

# Prompt the user to enter a seed for randomness
seed = input("Enter a seed for randomness (leave blank for no seed): ")
if seed:
    random.seed(seed)

# Choose a word list for section headings
heading_word_list = random.choice(list(word_lists.keys()))
heading_words = word_lists[heading_word_list]

# Load the sarneg word list
sarneg_path = os.path.join(word_list_directory, 'sarneg', 'sarneg.txt')
with open(sarneg_path, 'r') as file:
    sarneg_words = [line.strip() for line in file.readlines()]

# Select a random word for the authentication table
sarneg_word = random.choice(sarneg_words)

# Assign words to sections
assignments = assign_words(word_lists, sections, heading_word_list)

# Create Excel file
output_filename = 'assigned_words.xlsx'
create_excel(assignments, heading_words, sarneg_word, output_filename, sections_with_headings, word_lists)

print(f'Excel file "{output_filename}" created successfully.')
