import pandas as pd

df = pd.read_csv("../01_data/raw/week_2_3_exam_student_signals.csv")

df = df.drop_duplicates()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Unknown")

for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df[col] = df[col].fillna(df[col].mean())

df["Total Score"] = df["assignment_score"] + df["lab_score"]

df["Performance"] = df["attendance_pct"].apply(
    lambda x: "Good" if x >= 75 else "Needs Improvement"
)

df.to_csv("../01_data/processed/dataforge_cleaned.csv", index=False)

print("Done")