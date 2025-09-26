# Resume Analyzer

This is a web application that helps you optimize your resume for Applicant Tracking Systems (ATS). It analyzes your resume against a specific job role, identifies matching and missing keywords, and provides a match score.

## Features

- **Resume Analysis:** Upload your resume in PDF format.
- **Role-Based Analysis:** Select a job role to tailor the analysis.
- **Skill Matching:** See which skills from the job description are present or missing in your resume.
- **Match Score:** Get a percentage score indicating how well your resume matches the selected role.
- **Modern UI/UX:** A clean and modern user interface for a smooth experience.

## Technologies Used

- **Frontend:** React, Chart.js, Axios
- **Backend:** Flask, spaCy, PyMuPDF

## Setup and Installation

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install Flask flask_cors PyMuPDF spacy
    python -m spacy download en_core_web_sm
    ```

4.  **Run the Flask server:**
    ```bash
    python app.py
    ```
    The backend server will be running on `http://127.0.0.1:5000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../frontend/resume-ui
    ```

2.  **Install the required npm packages:**
    ```bash
    npm install
    ```

3.  **Run the React application:**
    ```bash
    npm start
    ```
    The frontend application will open in your browser at `http://localhost:3000`.

## How to Get a High ATS Score

An Applicant Tracking System (ATS) is an automated software that scans resumes for keywords, skills, and qualifications. Here are some tips to optimize your resume for ATS:

### 1. Use Relevant Keywords

-   **Analyze the Job Description:** Carefully read the job description and identify the key skills and qualifications the employer is looking for.
-   **Incorporate Keywords:** Naturally sprinkle these keywords throughout your resume, especially in the "Skills" and "Work Experience" sections.
-   **Use Both Acronyms and Full Forms:** For example, mention both "SQL" and "Structured Query Language".

### 2. Keep the Formatting Simple

-   **Use a Clean and Simple Layout:** Avoid using tables, columns, headers, and footers, as they can confuse the ATS.
-   **Use Standard Fonts:** Stick to common fonts like Arial, Calibri, or Times New Roman.
-   **Use Standard Section Headers:** Use clear and common section titles like "Work Experience," "Education," and "Skills."

### 3. Choose the Right File Type

-   **Use PDF or .docx:** Unless the job application specifies otherwise, submit your resume as a PDF or a Word document (.docx). These formats are generally well-parsed by ATS.

### 4. Include Your Contact Information

-   **Make it Easy to Find:** Place your name, phone number, email address, and LinkedIn profile URL at the top of your resume.

### 5. Tailor Your Resume for Each Application

-   **Don't Use a One-Size-Fits-All Resume:** Customize your resume for each job you apply for. This will ensure that you are including the most relevant keywords and qualifications for that specific role.

By following these tips, you can significantly increase your chances of getting your resume past the ATS and into the hands of a human recruiter.
