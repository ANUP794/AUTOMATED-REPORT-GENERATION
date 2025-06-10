import pandas as pd
from fpdf import FPDF

# Step 1: Read Data
df = pd.read_csv("data.csv")

# Step 2: Analyze Data
mean_score = df["Score"].mean()
max_score = df["Score"].max()
min_score = df["Score"].min()
total_students = df["Name"].count()

# Step 3: Create PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "CODTECH Internship Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(0, 10, "Automated Data Analysis Report", ln=True)

pdf.ln(10)
pdf.cell(0, 10, f"Total Students: {total_students}", ln=True)
pdf.cell(0, 10, f"Average Score: {mean_score:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Score: {max_score}", ln=True)
pdf.cell(0, 10, f"Lowest Score: {min_score}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Detailed Scores:", ln=True)
pdf.set_font("Arial", size=12)

# Add student scores
for index, row in df.iterrows():
    pdf.cell(0, 10, f"{row['Name']}: {row['Score']}", ln=True)

# Save PDF
pdf.output("Internship_Report.pdf")

print("✅ Report generated: Internship_Report.pdf")
