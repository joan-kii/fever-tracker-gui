import os
import csv
from datetime import datetime
from fpdf import FPDF # type: ignore


def new_track(name: str, temp: str, medicine: str, dose: str):

    """
    Create new track stored in a csv file
    :return: None
    """
    date: datetime = datetime.now()
    day: str = date.strftime("%d-%m-%Y")
    hour: str = date.strftime("%H:%M")
    path: str = "./csv_files/"
    file_path: str = os.path.join(path, f"{name}_{day}.csv")

    # Only accepts valid temperature
    if not 35.0 < float(temp) < 42.0:
        raise ValueError("Temperature has not a valid value")

    # Create csv file
    with open(file_path, "w", newline="") as track_file:
        fieldnames: list[str] = ["Name", "Date", "Hour", "Temperature", "Medicine", "Dose"]
        track_writer = csv.DictWriter(track_file, fieldnames=fieldnames)

        track_writer.writeheader()
        track_writer.writerow({
            "Name": name,
            "Date": day,
            "Hour": hour,
            "Temperature": temp,
            "Medicine": medicine,
            "Dose": dose
        })


def open_track(f: str) -> "list[list[str, str]]":

    """
    Open a track stored in the csv file
    :param f: csv file with track data
    :return: A list of dicts with data
    :rtype: list[dict[str, str]]
    """

    rows: list[list[str, str]] = []
    with open("./csv_files/" + f, "r") as track_file:
        track_reader = csv.reader(track_file)

        for row in track_reader:
            rows.append(row)

    return rows

def open_track_dict(f: str) -> "list[dict[str, str]]":

    """
    Open a track stored in the csv file
    :param f: csv file with track data
    :return: A list of dicts with data
    :rtype: list[dict[str, str]]
    """

    rows: list[dict[str, str]] = []
    with open("./csv_files/" + f, "r") as track_file:
        track_reader = csv.DictReader(track_file)

        for row in track_reader:
            rows.append(row)

    return rows

def add_row(f: str, temp: str, medicine: str, dose: str) -> None:

    """
    Add a row to the track stored in the csv file
    :param f: csv file with track data
    :return: None
    """

    date: datetime = datetime.now()
    day: str = date.strftime("%d-%m-%Y")
    hour: str = date.strftime("%H:%M")
    path: str = "./csv_files/"
    file_path: str = path + f

    # Only accepts valid temperature
    if not 35.0 < float(temp) < 42.0:
        raise ValueError("Temperature has not a valid value")

    # Add row to track
    with open(file_path, "a", newline="") as track_file:
        fieldnames: list[str] = ["Name", "Date", "Hour", "Temperature", "Medicine", "Dose"]
        track_writer = csv.DictWriter(track_file, fieldnames=fieldnames)

        track_writer.writerow({
            "Name": "",
            "Date": day,
            "Hour": hour,
            "Temperature": temp,
            "Medicine": medicine,
            "Dose": dose
        })


def convert_track(f):

    """
    Convert the csv file to a pdf file
    :param f: csv file with track data
    :return: None
    """
    
    # Get data
    data = open_track_dict(f) 

    # Format fieldnames
    format_name = "Name: " + data[0]["Name"].title()
    format_date = "Date: " + data[0]["Date"]

    # Delete no needed fields
    for row in data:
        del row["Name"]

    path: str = "./pdf_files/"

    # Create pdf file
    pdf = FPDF()
    pdf.add_page()

    # Add header
    pdf.set_font("Helvetica", size=16, style="BU")
    pdf.cell(w=180, h=30, txt="Fever Tracker", align="C", new_x="LMARGIN", new_y="NEXT")

    # Add patient info
    pdf.set_font("Helvetica", size=11)
    pdf.cell(w=80, h=8, txt=format_name, new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=80, h=8, txt=format_date, new_x="LMARGIN", new_y="NEXT")

    # Set cells sizes
    line_height: int = pdf.font_size * 2
    col_width: int = pdf.epw / 5

    pdf.ln(line_height)

    # Add fieldnames to table
    for field in data[0]:
        pdf.multi_cell(col_width, line_height, field, border=1, align="C",
            new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(line_height)

    # Add data cells
    pdf.set_font("Helvetica", size=10)
    for row in data:
        for d in row:
            pdf.multi_cell(col_width, line_height, row[d].title(), border=1, align="C",
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)

    # Create output pdf
    pdf.output(f"{path + f.strip('.csv')}.pdf")
    