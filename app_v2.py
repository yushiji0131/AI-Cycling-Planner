import streamlit as st
import pandas as pd
import datetime

# -----------------------------------------------------------------------------
# 1. Define the training plan data (Monday–Friday only).
#    Fill in the missing weeks (4–7) with your desired workouts.
# -----------------------------------------------------------------------------
training_plan = {
    "Week 1": {
        "Monday": {
            "workout_name": "Threshold Intervals",
            "duration": "1.5 hr",
            "description": (
                "Warm-up 10–15 min. 3×10 min @ 95–100% FTP (3–5 min recovery). "
                "Cool down 5–10 min."
            )
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2, light spin (<65% FTP)."
        },
        "Wednesday": {
            "workout_name": "Sweet Spot or Endurance",
            "duration": "1.5 hr",
            "description": (
                "Option A: 2×15 min @ 88–92% FTP (5 min rest). "
                "Option B: 1–1.5 hr @ Zone 2 if fatigued."
            )
        },
        "Thursday": {
            "workout_name": "VO₂ Max Intervals",
            "duration": "1.5 hr",
            "description": "5×3 min @ 110–115% FTP (3 min recovery)."
        },
        "Friday": {
            "workout_name": "Easy or Skills",
            "duration": "1 hr",
            "description": "Zone 1–2 spin or short sprints (4×10s) if feeling fresh."
        }
    },
    "Week 2": {
        "Monday": {
            "workout_name": "Threshold Intervals",
            "duration": "1.5 hr",
            "description": (
                "Warm-up 15 min. 2×15 min @ 95–100% FTP (5 min recovery). "
                "Cool down 10 min."
            )
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2, ~55–65% FTP."
        },
        "Wednesday": {
            "workout_name": "Sweet Spot",
            "duration": "1.5 hr",
            "description": "2×20 min @ ~90% FTP (5 min rest)."
        },
        "Thursday": {
            "workout_name": "VO₂ Max",
            "duration": "1.5 hr",
            "description": "6×3 min @ 110–115% FTP (3 min recovery)."
        },
        "Friday": {
            "workout_name": "Easy or Light Sprints",
            "duration": "1 hr",
            "description": "Zone 1–2 spin or 4×10s sprints."
        }
    },
    "Week 3": {
        "Monday": {
            "workout_name": "Threshold Intervals",
            "duration": "1.5 hr",
            "description": (
                "3×12 min @ 98–102% FTP (4–5 min recovery). Warm-up/cool down as needed."
            )
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2, easy pedal."
        },
        "Wednesday": {
            "workout_name": "Sweet Spot or Endurance",
            "duration": "1.5 hr",
            "description": "2×20 min @ 90–95% FTP or 1.5 hr @ Zone 2."
        },
        "Thursday": {
            "workout_name": "VO₂ Max",
            "duration": "1.5 hr",
            "description": "5×4 min @ 110–115% FTP (4–5 min recovery)."
        },
        "Friday": {
            "workout_name": "Easy Spin",
            "duration": "1 hr",
            "description": "Zone 1–2 or off if feeling depleted."
        }
    },
    "Week 4": {
        "Monday": {
            "workout_name": "Threshold - Reduced Volume",
            "duration": "1 hr",
            "description": "2×10 min @ 90–95% FTP (5 min rest). Recovery week load."
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2, light spin."
        },
        "Wednesday": {
            "workout_name": "Endurance",
            "duration": "1 hr",
            "description": "1 hr steady Zone 2 (65–75% FTP)."
        },
        "Thursday": {
            "workout_name": "Short VO₂ Max",
            "duration": "1 hr",
            "description": "4×2 min @ 110–115% FTP (3 min recovery)."
        },
        "Friday": {
            "workout_name": "Easy or Off",
            "duration": "1 hr",
            "description": "Very light spin or day off if needed."
        }
    },
    "Week 5": {
        "Monday": {
            "workout_name": "Threshold Intervals",
            "duration": "1.5 hr",
            "description": "3×12 min @ 100–105% FTP (5 min recovery)."
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2 spin."
        },
        "Wednesday": {
            "workout_name": "Sweet Spot",
            "duration": "1.5 hr",
            "description": "2×20 min @ 90–95% FTP (5 min rest)."
        },
        "Thursday": {
            "workout_name": "VO₂ Max",
            "duration": "1.5 hr",
            "description": "6×3 min @ 110–120% FTP (3 min rest)."
        },
        "Friday": {
            "workout_name": "Easy Spin",
            "duration": "1 hr",
            "description": "Zone 1–2 or short sprints if fresh."
        }
    },
    "Week 6": {
        "Monday": {
            "workout_name": "Threshold Intervals",
            "duration": "1.5 hr",
            "description": "2×20 min @ 100–105% FTP (5 min recovery)."
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2 spin."
        },
        "Wednesday": {
            "workout_name": "Endurance/Sweet Spot",
            "duration": "1.5 hr",
            "description": "1.5 hr @Z2 or 2×10 min @SS if fresh."
        },
        "Thursday": {
            "workout_name": "VO₂ Max",
            "duration": "1.5 hr",
            "description": "4×5 min @ 110–115% FTP (5 min recovery)."
        },
        "Friday": {
            "workout_name": "Easy Spin",
            "duration": "1 hr",
            "description": "Zone 1–2 or off if needed."
        }
    },
    "Week 7": {
        "Monday": {
            "workout_name": "Threshold - Tapered",
            "duration": "1–1.25 hr",
            "description": "2×10 min @ 90–95% FTP."
        },
        "Tuesday": {
            "workout_name": "Easy Recovery Spin",
            "duration": "1 hr",
            "description": "Zone 1–2."
        },
        "Wednesday": {
            "workout_name": "Endurance",
            "duration": "1–1.25 hr",
            "description": "Mostly Z2, a short SS if feeling good."
        },
        "Thursday": {
            "workout_name": "Short VO₂",
            "duration": "1–1.25 hr",
            "description": "4×2 min @ 110–115% FTP (3 min rest)."
        },
        "Friday": {
            "workout_name": "Easy Spin",
            "duration": "1 hr",
            "description": "Zone 1–2 or off if needed."
        }
    },
    "Week 8": {
        "Monday": {
            "workout_name": "Threshold Opener",
            "duration": "1 hr",
            "description": "2×8 min @ 95–100% FTP. Short WU/CD."
        },
        "Tuesday": {
            "workout_name": "Easy Spin",
            "duration": "1 hr",
            "description": "Zone 1–2, keep it light."
        },
        "Wednesday": {
            "workout_name": "Endurance",
            "duration": "1 hr",
            "description": "Zone 2, ~60 min steady."
        },
        "Thursday": {
            "workout_name": "FTP Test",
            "duration": "Varies",
            "description": "Warm-up 20 min, 20-min all-out or ramp test, then cool down."
        },
        "Friday": {
            "workout_name": "Recovery Spin / Off",
            "duration": "0.5–1 hr",
            "description": "Zone 1 or day off if needed."
        }
    }
}

# -----------------------------------------------------------------------------
# 2. Set up session state for daily logs (notes, weight, HRV, resting HR).
# -----------------------------------------------------------------------------
# We'll store data in a nested dictionary structure in st.session_state.
# Keys will be (week, day) pairs, each mapping to a dictionary of user inputs.

if "daily_logs" not in st.session_state:
    # Initialize the structure
    # daily_logs[(week, day)] = {
    #   "notes": str,
    #   "weight": float,
    #   "hrv": float,
    #   "rhr": float
    # }
    st.session_state.daily_logs = {}

# -----------------------------------------------------------------------------
# 3. Streamlit App Layout
# -----------------------------------------------------------------------------

st.title("8-Week FTP Improvement Plan (Indoor: Mon–Fri)")
st.markdown(
    """
This app presents your Monday–Friday training plan for 8 weeks and 
allows you to log **daily results** such as notes, weight, HRV, and resting HR.

- **Saturday** (Outdoor ride) and **Sunday** (Rest) are not displayed here.
- **Data** you enter is saved in-memory (i.e., it will be lost if you refresh or close the app).
- Use the **Download CSV** button at the bottom to save your logs externally.
"""
)

# ------------------------------------------------------------------------
# 3.1 Display each week's plan + Input fields for user logs
# ------------------------------------------------------------------------

for week_number, weekly_schedule in training_plan.items():
    # Create an expander for each week
    with st.expander(week_number, expanded=False):
        st.subheader(f"{week_number} – Monday to Friday Workouts")
        
        for day_name, workout_info in weekly_schedule.items():
            day_key = (week_number, day_name)
            
            # Show the planned workout
            st.write(f"**{day_name}**: {workout_info['workout_name']} | {workout_info['duration']}")
            st.caption(workout_info["description"])
            
            # Retrieve existing log data (if any)
            if day_key not in st.session_state.daily_logs:
                st.session_state.daily_logs[day_key] = {
                    "notes": "",
                    "weight": 0.0,
                    "hrv": 0.0,
                    "rhr": 0.0
                }
            
            # Display inputs for daily logs
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                # Weight
                new_weight = st.number_input(
                    f"Weight (kg) - {day_name}",
                    min_value=0.0, max_value=200.0, step=0.1,
                    key=f"{week_number}_{day_name}_weight",
                    value=st.session_state.daily_logs[day_key]["weight"]
                )
            with col2:
                # HRV
                new_hrv = st.number_input(
                    f"HRV - {day_name}",
                    min_value=0.0, max_value=300.0, step=1.0,
                    key=f"{week_number}_{day_name}_hrv",
                    value=st.session_state.daily_logs[day_key]["hrv"]
                )
            with col3:
                # Resting HR
                new_rhr = st.number_input(
                    f"RHR - {day_name}",
                    min_value=0.0, max_value=200.0, step=1.0,
                    key=f"{week_number}_{day_name}_rhr",
                    value=st.session_state.daily_logs[day_key]["rhr"]
                )
            with col4:
                # We won't put anything in the 4th column in this example,
                # but you could add more metrics here if desired.
                pass
            
            # Notes text area
            new_notes = st.text_area(
                f"Notes - {day_name}",
                key=f"{week_number}_{day_name}_notes",
                value=st.session_state.daily_logs[day_key]["notes"]
            )
            
            # Update session state with any changes
            st.session_state.daily_logs[day_key]["weight"] = new_weight
            st.session_state.daily_logs[day_key]["hrv"] = new_hrv
            st.session_state.daily_logs[day_key]["rhr"] = new_rhr
            st.session_state.daily_logs[day_key]["notes"] = new_notes
            
            st.markdown("---")

# ------------------------------------------------------------------------
# 4. Button to download daily logs as CSV
# ------------------------------------------------------------------------

st.header("Download Your Training Logs")
st.markdown(
    "Once you've entered your data, click **Download CSV** to save your "
    "logs. Remember that your inputs won't persist after you close or "
    "refresh the app (unless you implement a database)."
)

def convert_logs_to_csv():
    """
    Convert st.session_state.daily_logs (nested dict) into a pandas DataFrame,
    then return a CSV string.
    """
    rows = []
    for (week, day), metrics in st.session_state.daily_logs.items():
        rows.append({
            "Week": week,
            "Day": day,
            "Weight": metrics["weight"],
            "HRV": metrics["hrv"],
            "Resting_HR": metrics["rhr"],
            "Notes": metrics["notes"]
        })
    df = pd.DataFrame(rows)
    return df.to_csv(index=False)

if st.button("Download CSV"):
    csv_data = convert_logs_to_csv()
    
    # Create a downloadable link
    st.download_button(
        label="Click to Download",
        data=csv_data,
        file_name=f"training_logs_{datetime.date.today()}.csv",
        mime="text/csv"
    )
