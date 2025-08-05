# OncoDex

OncoDex is a simple yet powerful web application for biomedical researchers and clinicians to **upload**, **preview**, and **analyse** experimental and clinical datasets. It provides quick access to summary statistics and basic visualisations to facilitate **exploratory data analysis (EDA)** — without writing code.

> Final project for [CS50x – Harvard's Introduction to Computer Science](https://cs50.harvard.edu/x/)

---

## Features

- Upload multiple `.csv` datasets
- Preview tabular data directly in the browser
- View summary statistics (mean, SD, min, max, etc.)
- Automatically generate **bar plots** of means ± standard deviations for all numeric columns
- Clean, responsive UI styled with custom CSS
- Safe file handling and server-side validation

---

## Tech Stack

| Layer        | Tool        |
|--------------|-------------|
| Backend      | Python + Flask |
| Frontend     | HTML + Jinja2 Templates + CSS |
| Data         | Pandas |
| Plotting     | Matplotlib |
| Deployment   | Localhost (`Flask` dev server) |
| File Storage | `uploads/` folder (temp CSV storage) |

---

## Requirements

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

requirements.txt
```
Flask==2.3.2
pandas==2.0.3
matplotlib==3.7.1
Werkzeug==2.3.7
```

---

## Project Structure
```
OncoDex/
├── app.py                     # Flask app
├── requirements.txt
├── uploads/                   # Uploaded CSVs (temporary)
│   ├── dummy_data.csv
│   └── dummy_data2.csv
├── static/
│   └── styles.css             # Custom styling
├── templates/                 # HTML templates
│   ├── layout.html            # Base layout
│   ├── index.html             # Home
│   ├── upload.html            # Upload form
│   ├── upload_confirmation.html
│   ├── analyse.html           # Data preview and stats
│   └── about.html             # About section
```

---

## Usage
Start the app:
```bash
python app.py
```

Then open your browser and go to:
> http://127.0.0.1:5000

---

## Navigation

| Page    | URL Path  | Description                          |
|---------|-----------|--------------------------------------|
| Home    | `/`       | Welcome screen                       |
| Upload  | `/upload` | Upload a CSV                         |
| Analyse | `/analyse`| Select and analyse uploaded CSVs     |
| About   | `/about`  | Instructions & app overview          |

---

## Example Output
After uploading a dataset, OncoDex automatically:
- Displays the first five rows
- Generates summary statistics (mean, std, min, max, etc.)
- Plots mean ± standard deviation for numeric columns
(Rendered inline via base64-encoded PNG)

---

## Why I Built This

I created OncoDex as a final project for CS50x to bring together key programming concepts:
- Routing and form handling in Flask
- File upload and sanitisation
- Data parsing and visualisation with Pandas/Matplotlib
- HTML templating with Jinja2
- Basic frontend styling with CSS

---

## Possible Extensions
- Add scatterplots or histograms
- Export summary stats or plots as files
- Add filtering/search for data columns
- Integrate user authentication (login/logout)

---

![Python](https://img.shields.io/badge/Built_with-Python_3.10-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![Pandas](https://img.shields.io/badge/Data-Pandas-yellow)
![Matplotlib](https://img.shields.io/badge/Plots-Matplotlib-orange)
![CS50](https://img.shields.io/badge/CS50x-Project-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Beta-yellow)
