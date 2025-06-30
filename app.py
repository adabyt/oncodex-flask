import base64
import io
import os
import matplotlib
matplotlib.use('Agg') # Prevents a crash in Safari when trying to analyse data
import matplotlib.pyplot as plot
import pandas as pd

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    return render_template("index.html")


# Upload documents
@app.route("/upload", methods=["GET", "POST"])
def upload():
    file = request.files.get("file")

    # If no file has been uploaded or if file is not a csv file
    if not file or file.filename == "" or not file.filename.endswith(".csv"):
        return render_template("upload.html", message="Please upload a CSV file.", uploaded_files=[])
    
    if request.method == "POST":
        # Prevent any potential malicious naming
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        # List of uploaded files
        uploaded_files = [file for file in os.listdir(UPLOAD_FOLDER) if not file.startswith('.')]

        return render_template("upload_confirmation.html", message="File uploaded successfully.", uploaded_files=uploaded_files)
    
    # For a GET request
    return render_template("upload.html")


# Analyse Data
@app.route("/analyse", methods=["GET", "POST"])
def analyse():
    uploaded_files = [file for file in os.listdir(UPLOAD_FOLDER) if file.endswith('.csv')]

    # If no data has been uploaded
    if not uploaded_files:
        message = "No data uploaded. Please upload a CSV file."
        return render_template("analyse.html", message=message, files=uploaded_files)

    if request.method == "POST":
        selected_file = request.form.get("selected_file")
        if selected_file not in uploaded_files:
            message = "Invalid file selected."
            return render_template("analyse.html", message=message, files=uploaded_files)

        # Read the data as a data frame
        df = pd.read_csv(os.path.join(UPLOAD_FOLDER, selected_file))

        # Generate preview of the data and show summary stats
        preview_html = df.head().to_html(classes='table table-striped', index=False)
        summary_html = df.describe().to_html(classes='table table-bordered')

        # Create a bar plot showing mean ± standard deviation for numeric columns
        img = io.BytesIO()
        numeric_cols = df.select_dtypes(include='number').columns

        # Only make a plot if there are numeric values in the data
        if len(numeric_cols) > 0:
            means = df[numeric_cols].mean()
            stds = df[numeric_cols].std()

            plot.figure(figsize=(8, 5))
            plot.bar(means.index, means.values, yerr=stds.values, capsize=8, color='#007bff', edgecolor='black')
            plot.ylabel('Mean Value', fontsize=12)
            plot.title(f'Mean ± Std Dev for Numeric Columns in {selected_file}', fontsize=14, fontweight='bold')
            plot.xticks(rotation=45, ha='right')
            plot.tight_layout()

            # Save file in memory not on disk
            plot.savefig(img, format='png')
            # Prevent memory leaks
            plot.close()
            # Read image from start
            img.seek(0)
            # Convert to UTF-8 to directly use in .html file as img src
            plot_url = base64.b64encode(img.getvalue()).decode()
        else:
            plot_url = None

        return render_template(
            "analyse.html",
            files=uploaded_files,
            preview=preview_html,
            summary=summary_html,
            plot_url=plot_url,
            selected_file=selected_file
        )

    # For a GET request
    return render_template("analyse.html", files=uploaded_files)


# About section
@app.route("/about")
def about():
    return render_template("about.html")
