from analyzer import analyze_csv 
df, summary = analyze_csv("test.csv")

print("DATA: ")
print(df)

print("\nSUMMARY:")
print(summary)