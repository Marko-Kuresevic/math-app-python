import csv

def create_mult_table():
    matrix = []
    table_str = ""

    for i in range(0, 10):
        row = ""
        for j in range(0, 10):
            num1, num2 = i + 1, j + 1
            mult = num1 * num2

            matrix.append([num1, num2, mult])

            row += f"{num2} x {num1:2} = "
            if num2 == 10:
                row += f"{mult:3}"
            else: row += f"{mult:2}"
            row += "   "
        table_str += row + "\n"

    header = ["Multiplicand", "Multiplier", "Product"]

    with open("math_app/data/multiplication_table.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(matrix)
    
    return table_str

if __name__ == "__main__":
    create_mult_table()