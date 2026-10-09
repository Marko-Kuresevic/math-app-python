def compute_gcd_lcm(num1, num2):
    num_prime_list = []
    for_print = f"({num1}, {num2}) = "
    gcd = lcm = 1

    lower = min(num1, num2)

    for i in range(2, lower // 2 + 1):
        x = 2

        while x < i and i % x != 0:
            x += 1

        if x == i:
            while num1 % x == 0 and num2 % x == 0:
                num_prime_list.append((num1, num2, x))

                if gcd == 1:
                    for_print += f"{x}"
                else: for_print += f" x {x}"

                num1 //= x
                num2 //= x

                gcd *= x
            
    num_prime_list.append((num1, num2, ""))

    lcm = gcd * num1 * num2

    for_print_gcd = f"GCD{for_print} = {gcd}"
    for_print_lcm = f"LCM{for_print} x {num1} x {num2} = {lcm}"

    result = (num_prime_list, for_print_gcd, for_print_lcm)

    return result

if __name__ == "__main__":
    compute_gcd_lcm()