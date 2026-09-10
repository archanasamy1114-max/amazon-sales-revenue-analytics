import pandas as pd

# Load original dataset
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Remove unnecessary columns
df = df.drop(columns=["index", "Unnamed: 22"], errors="ignore")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Fill missing Amount values
df["Amount"] = df["Amount"].fillna(0)

# Create cancellation flag
df["Is_Cancelled"] = df["Status"].astype(str).str.contains(
    "Cancelled",
    case=False,
    na=False
).astype(int)

# Remove completely empty rows
df = df.dropna(how="all")

# Save cleaned dataset
df.to_csv("Cleaned_Amazon_Sales.csv", index=False)

# Check result
print("Cleaned Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nCancelled Orders:", df["Is_Cancelled"].sum())

print("\nCleaned file created successfully!")