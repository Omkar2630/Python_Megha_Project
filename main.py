import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("bcm_testcases.xlsx")

# Counters
pass_count = 0
fail_count = 0

# Open files
log_file = open("execution_log.txt", "w")
report_file = open("report.txt", "w")

print("Starting BCM Testing...\n")

# Execute test cases
for index, row in df.iterrows():

    test_input = row["Input"]
    expected = row["Expected"]

    # BCM Logic
    if test_input == "lock":
        actual = "Door Locked"

    elif test_input == "unlock":
        actual = "Door Unlocked"

    else:
        actual = "Invalid Input"

    # Compare result
    if actual == expected:
        status = "PASS"
        pass_count += 1
    else:
        status = "FAIL"
        fail_count += 1

    # Result message
    result = f"{row['TC_ID']} --> {status}"

    print(result)

    # Write log
    log_file.write(result + "\n")

    # Write report
    report_file.write(
        f"{row['TC_ID']} | Expected: {expected} | Actual: {actual} | Status: {status}\n"
    )

# Close files
log_file.close()
report_file.close()

# Total test cases
total = pass_count + fail_count

print("\nTesting Completed")
print(f"Total Test Cases : {total}")
print(f"PASS : {pass_count}")
print(f"FAIL : {fail_count}")

# Pie chart
labels = ["PASS", "FAIL"]
values = [pass_count, fail_count]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("BCM Test Result")

# Save chart
plt.savefig("chart.png")

# Show chart
plt.show()