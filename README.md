# Result Management System

A comprehensive Django-based web application designed to automate the processing, management, and analysis of university student results. This system eliminates manual data entry by extracting marks directly from PDF result sheets.

## � Project Explanation

The **Result Management System** is built to bridge the gap between static PDF result sheets and dynamic data analysis. In many universities, results are published as PDF documents, making it difficult to perform aggregate analysis or generate custom reports. This application solves that problem by automating the extraction and storage of this data.

### How It Works

1.  **Data Ingestion (PDF Parsing)**
    *   **Upload**: A student logs in and uploads their result PDF.
    *   **Conversion**: The backend utilizes `pdftotext.exe` (an external command-line tool) to convert the PDF into a raw text file while preserving the physical layout (tables, columns).
    *   **Parsing Logic**: A custom parser reads the text file. It relies on a configuration file named `rule.xlsx`, which contains specific Regex patterns and keywords (e.g., "Semester", "Total Marks"). This allows the system to identify and extract relevant data points like USN, Subject Codes, Internal/External Marks, and Pass/Fail status purely through pattern matching.

2.  **Data Storage**
    *   The extracted data is cleaned and stored in a relational database (SQLite).
    *   The system links marks to specific **Students**, **Batches**, and **Branches**, enabling hierarchical data organization.

3.  **Analytics & Visualization**
    *   **Professor Dashboard**: Professors can access a holistic view of the performance. The system calculates pass percentages, grade distributions (FCD, FC, SC), and subject-wise failure rates on the fly.
    *   **Visuals**: It uses `Matplotlib` (with the Agg backend) to generate bar charts and pie charts that visualize these statistics, helping faculty identify difficult subjects or underperforming batches.

4.  **Reporting**
    *   The system automates the generation of official result sheets. Using `OpenPyXL`, it formats the database records into a professional Excel report with proper headers, merged cells, and borders, ready for printing or archival.

## 🚀 Key Features

*   **Automated PDF Parsing**: Upload result PDFs, and the system automatically extracts USN, Subjects, Marks, and Results.
*   **Role-Based Access**:
    *   **Students**: Upload result documents, view marks, and track performance.
    *   **Professors**: Access detailed analytics, view class performance, and generate reports.
*   **Analytics Dashboard**: Visual insights into subject-wise performance and pass/fail distributions using dynamic charts.
*   **Excel Reporting**: Generate professional-grade Excel reports for batches and semesters with a single click.
*   **Data Management**: Structured database for Departments (Branches), Batches, and Semesters.

## 🛠️ Tech Stack

*   **Backend**: Django (Python 3.x)
*   **Database**: SQLite (Default)
*   **Frontend**: HTML, CSS, Bootstrap
*   **Data Processing**: Pandas, OpenPyXL, Regex
*   **Visualization**: Matplotlib
*   **PDF Engine**: XpdfReader (pdftotext)

## 📂 Project Structure

*   `result_management/`: Core settings and configuration.
*   `professor/`: Handles professor dashboards, analytics, and Excel generation.
*   `student/`: Manages student uploads (PDF parsing logic) and result views.
*   `users/`: Custom user models and authentication (Login/Register).
*   `media/`: Stores uploaded PDFs and generated Excel reports.
*   `static/`: CSS, Images, and Javascript files.
*   `pdftotext.exe`: Executable used for PDF to Text conversion.
*   `rule.xlsx`: Configuration file containing parsing rules for different result formats.

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/abhighali79/Student_result_analysis.git
    ```

2.  **Install Dependencies**
    ```bash
    pip install django pandas openpyxl matplotlib pillow
    ```

3.  **Database Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create Superuser** (Admin Access)
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```
    Access the application at `http://127.0.0.1:8000/`.

## ⚠️ Important Note

*   **PDF Parsing Engine**: The project requires `pdftotext.exe` to be present in the root directory for parsing to work.
*   **Rule Configuration**: The parsing logic is data-driven by `rule.xlsx`. Changes to the PDF format can often be handled by updating this Excel file without rewriting code.
