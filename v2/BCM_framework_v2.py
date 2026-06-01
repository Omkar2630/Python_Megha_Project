import pandas as pd
import matplotlib.pyplot as plt

# Read Excel File
df = pd.read_excel(r"C:\Users\sg97976\Desktop\Mega_Project\Python_Megha_Project\v2\test_case_v2.xlsx")

pass_count = 0
fail_count = 0

# Open files
log_file = open("execution_log_V2.txt", "w")
report_file = open("report.txt_V2", "w")

# BCM Logic Function
def bcm_logic(action, speed, door_status):

    # Negative speed check
    if speed < 0:
        return "Error"

    # Lock operation
    if action == "lock":
        return "Door Locked"

    # Unlock operation
    elif action == "unlock":

        if speed > 60:
            return "Door Locked"

        return "Door Unlocked"

    # Auto Lock operation
    elif action == "auto_lock":

        if speed > 20 and door_status == "Closed":
            return "Door Locked"

        return "Door Unlocked"

    # Invalid command
    else:
        return "Invalid Input"


# Execute Test Cases
for index, row in df.iterrows():

    tc_id = row["TC_ID"]
    action = row["Action"]
    speed = row["Speed"]
    door_status = row["Door_Status"]
    expected = row["Expected"]

    actual = bcm_logic(action, speed, door_status)

    # PASS / FAIL
    if actual == expected:
        status = "PASS"
        pass_count += 1
    else:
        status = "FAIL"
        fail_count += 1

    result = f"{tc_id} --> {status}"

    print(result)

    # Write Log
    log_file.write(result + "\n")

    # Write Report
    report_file.write(
        f"{tc_id} | Action: {action} | Speed: {speed} | "
        f"Door Status: {door_status} | "
        f"Expected: {expected} | Actual: {actual} | {status}\n"
    )

# Close files
log_file.close()
report_file.close()

# Summary
total_tests = pass_count + fail_count

# print("\n===== TEST SUMMARY =====")
# print(f"Total Test Cases : {total_tests}")
# print(f"PASS             : {pass_count}")
# print(f"FAIL             : {fail_count}")

# Pie Chart
labels = ["PASS", "FAIL"]
values = [pass_count, fail_count]

plt.figure(figsize=(6, 6))

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    explode=[0, 0.1],
    shadow=True
)

plt.title("BCM Door Lock Test Results")

plt.savefig("bcm_test_report_chart.png")
# plt.show()

print("\nTesting Completed Successfully")