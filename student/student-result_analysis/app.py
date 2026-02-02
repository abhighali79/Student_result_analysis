from flask import Flask, request, redirect, url_for, send_file, flash, render_template, session
import os
from werkzeug.utils import secure_filename
import pdfplumber
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
UPLOAD_FOLDER = 'uploads'  # Directory for uploaded PDFs
OUTPUT_FOLDER = 'output'  # Directory for storing CSV files
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Dummy login credentials for faculty
FACULTY_USERNAME = "faculty"
FACULTY_PASSWORD = "password"

# Helper functions for PDF extraction
def extract_usn_from_pdf(pdf_path):
    usn = None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    if "USN" in line:
                        usn = line.split("USN:")[-1].strip()
                        break
    return usn

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

def generate_combined_csv(results_folder, output_path):
    csv_filename = os.path.join(output_path, 'combined_results.csv')
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["USN", "Subject Code", "Subject Name", "Internal Marks", "External Marks", "Total", "Result", "Date"])
        
        for result_pdf in os.listdir(results_folder):
            if result_pdf.endswith('.pdf'):
                pdf_path = os.path.join(results_folder, result_pdf)
                usn = extract_usn_from_pdf(pdf_path)
                result_data = extract_result_data_from_pdf(pdf_path)

                for row in result_data:
                    writer.writerow([usn] + row)

    return csv_filename

# Route definitions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part", "danger")
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash("No selected file", "danger")
            return redirect(request.url)

        if file:
            # Save the uploaded file
            file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(file_path)
            flash("File successfully uploaded", "success")
            return redirect(url_for('upload_file'))

    # Render the upload form for GET requests
    return render_template('upload.html')

@app.route('/faculty', methods=['GET', 'POST'])
def faculty_dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            csv_file = generate_combined_csv(UPLOAD_FOLDER, OUTPUT_FOLDER)
            return send_file(csv_file, as_attachment=True)
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
            return redirect(url_for('faculty_dashboard'))

    return render_template('faculty.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == FACULTY_USERNAME and password == FACULTY_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('faculty_dashboard'))
        else:
            flash('Invalid credentials. Please try again.', "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
