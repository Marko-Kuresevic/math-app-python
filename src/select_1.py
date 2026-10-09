import csv

def get_products(divisor, odd, even):
    with open("math_app/data/multiplication_table.csv", "r", newline = "") as file:
        reader = csv.reader(file)
        next(reader)

        product_list = []

        for row in reader:
            multiplicand = int(row[0].strip())
            product = int(row[2].strip())

            if multiplicand == divisor:
                if odd and even:
                    product_list.append(product)
                else:
                    if (odd and product % 2 != 0) or (even and product % 2 == 0):
                        product_list.append(product)

    return product_list

if __name__ == "__main__":
    get_products()