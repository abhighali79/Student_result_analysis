import pdfplumber
import csv
import os

def extract_University_Seat_Number_from_pdf(pdf_path):
    University_Seat_Number = None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    if "University Seat Number" in line:
                        University_Seat_Number = line.split("University Seat Number:")[-1].strip()
                        break
    return University_Seat_Number

def extract_result_data_from_pdf(pdf_path):
    result_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 6 and parts[0][:2].isdigit():
                        subject_code = parts[0]
                        subject_name = ' '.join(parts[1:-5])
                        internal_marks = parts[-5]
                        external_marks = parts[-4]
                        total = parts[-3]
                        result = parts[-2]
                        date = parts[-1] if len(parts) > 6 else ''
                        result_data.append([subject_code, subject_name, internal_marks, external_marks, total, result, date])
    return result_data

def save_to_csv(data, output_csv):
    headers = ["University Seat Number", "Subject Code", "Subject Name", "Internal Marks", "External Marks", "Total Marks", "Result", "Date"]
    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
