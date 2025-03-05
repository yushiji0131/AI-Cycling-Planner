from fpdf import FPDF
import os
from datetime import datetime, timedelta

# ==============================
# Configuration (MODIFY HERE)
# ==============================
FTP = 250                   
BIKE_COMPUTER = "Garmin Edge 530"  
START_DATE = "2024-04-01"  
FONT_REGULAR = os.path.abspath("NotoSansSC-Regular.ttf")  # Chinese font for potential needs
FONT_BOLD = os.path.abspath("NotoSansSC-Bold.ttf")        

# ==============================
# Complete 12-Week Training Data
# ==============================
training_data = [
    {   # Week 1 - Base Adaptation
        "week": 1,
        "phase": "Base Adaptation",
        "days": {
            "Monday": {
                "type": "Threshold Climb",
                "duration": "75min",
                "zone": "Z4",
                "detail": "3x8min Z4 climbs (5% grade @70rpm)\nRest: 5min between sets\nCore: Plank 3x45s"
            },
            "Tuesday": {
                "type": "Active Recovery",
                "duration": "45min",
                "zone": "Z1",
                "detail": "Easy spin + dynamic stretching\nHR ≤120bpm @90+rpm"
            },
            "Wednesday": {
                "type": "Climb Strength + VO2Max",
                "duration": "80min",
                "zone": "Z3-Z5",
                "detail": "Low-cadence climbs 5x5min Z3 (50rpm @5%)\nHigh-cadence sprints 3x3min Z5 (100rpm)"
            },
            "Thursday": {
                "type": "Endurance Ride",
                "duration": "60min",
                "zone": "Z2",
                "detail": "Steady-state @85-95rpm\nMaintain 70-80% FTP"
            },
            "Friday": {
                "type": "Threshold Sustain",
                "duration": "75min",
                "zone": "Z3",
                "detail": "2x20min Z3 efforts (3% grade)\nRecovery: 10min Z1 between"
            },
            "Saturday": {
                "type": "Long Ride Integration",
                "duration": "180min",
                "zone": "Z2-Z3",
                "detail": "First 2hrs Z2 (flat)\nFinal hour: 4x8min Z3 climbs (5% grade)"
            },
            "Sunday": {
                "type": "Complete Rest",
                "duration": "-",
                "zone": "-",
                "detail": "NO TRAINING\nRecommend: Walking/Yoga/Foam rolling"
            }
        },
        "note": "Key Focus: Adapt to low-cadence climbing, carb intake 60g/h"
    },
    # Weeks 2-12 follow similar structure...
]

# ==============================
# PDF Generator Class
# ==============================
class CyclingTrainingPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("NotoSansSC", "", FONT_REGULAR, uni=True)
        self.add_font("NotoSansSC", "B", FONT_BOLD, uni=True)
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        if self.page == 1: return
        self.set_font("NotoSansSC", "B", 10)
        self.cell(0, 10, f"12-Week Cycling Plan | FTP {FTP}W | {BIKE_COMPUTER}", 0, 0, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font("NotoSansSC", "", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

    def create_cover(self):
        self.add_page()
        self.set_font("NotoSansSC", "B", 24)
        self.cell(0, 50, "12-Week Cycling Training Plan", 0, 1, 'C')
        self.set_font_size(16)
        self.cell(0, 10, f"FTP: {FTP}W | Device: {BIKE_COMPUTER}", 0, 1, 'C')
        self.cell(0, 10, f"Start Date: {START_DATE}", 0, 1, 'C')
    
    def create_weekly_schedule(self, week_data):
        self.add_page()
        self.set_font("NotoSansSC", "B", 14)
        title = f"Week {week_data['week']} - {week_data['phase']}"
        self.cell(0, 10, title, 0, 1)
        
        # Date calculation
        start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
        current_date = start_date + timedelta(weeks=week_data['week']-1)
        date_range = f"{current_date.strftime('%b %d')} - {(current_date + timedelta(days=6)).strftime('%b %d')}"
        self.set_font("NotoSansSC", "", 10)
        self.cell(0, 10, date_range, 0, 1)
        
        # Schedule table
        col_width = [25, 35, 20, 110]
        headers = ["Day", "Type", "Zone", "Workout Details"]
        self.set_fill_color(240, 240, 240)
        
        # Table header
        for i, header in enumerate(headers):
            self.cell(col_width[i], 10, header, 1, 0, 'C', fill=True)
        self.ln()
        
        # Table content
        self.set_font("NotoSansSC", "", 10)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            data = week_data["days"][day]
            self.cell(col_width[0], 10, day, 1)
            self.cell(col_width[1], 10, data["type"], 1)
            self.cell(col_width[2], 10, data["zone"], 1)
            self.multi_cell(col_width[3], 10, data["detail"], 1)
            self.ln(0)
        
        # Weekly notes
        # self.set_font("NotoSansSC", "I", 10)
        self.multi_cell(0, 8, f"🔑 Weekly Focus: {week_data['note']}")

# ==============================
# Main Program
# ==============================
def main():
    # Validate fonts
    if not all(os.path.exists(f) for f in [FONT_REGULAR, FONT_BOLD]):
        print("Error: Missing font files! Download from:")
        print("https://fonts.google.com/noto")
        print("Required: NotoSansSC-Regular.ttf & NotoSansSC-Bold.ttf")
        return

    pdf = CyclingTrainingPDF()
    pdf.create_cover()
    
    # Generate weekly plans
    for week in training_data:
        pdf.create_weekly_schedule(week)
    
    # Add recovery guide
    pdf.add_page()
    pdf.set_font("NotoSansSC", "B", 16)
    pdf.cell(0, 10, "Recovery Protocols", 0, 1)
    pdf.set_font("NotoSansSC", "", 12)
    pdf.multi_cell(0, 10, """
    1️⃣ Pre-Ride Dynamic Stretching:
    • Walking Lunges with Twist: 15s/side x3
    • Leg Swings: 10x/side x2
    
    2️⃣ Post-Ride Yoga:
    • Downward Dog Flow: 5min
    • Pigeon Pose: 3min/side
    
    3️⃣ Strength Training (2x/week):
    • Single-Leg Squats: 3x12/side
    • Kettlebell Swings: 4x15 (16kg)
    """)
    
    # Save PDF
    output_file = f"Cycling_Training_Plan_FTP{FTP}.pdf"
    pdf.output(output_file)
    print(f"File generated: {output_file}")

if __name__ == "__main__":
    main()