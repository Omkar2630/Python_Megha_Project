import matplotlib.pyplot as plt


class ChartGenerator:

    @staticmethod
    def generate(pass_count, fail_count, output_file):

        labels = ["Pass", "Fail"]
        sizes = [pass_count, fail_count]

        plt.figure(figsize=(6, 6))

        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title("BCM Test Execution Summary")

        plt.savefig(output_file)

        plt.close()