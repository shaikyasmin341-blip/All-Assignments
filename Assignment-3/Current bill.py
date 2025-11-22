#Write a Python program to calculate the TGNPDCL electricity bill based on previous and current readings and type of customer.
#print the values of EC=224.60, FC=20.00, CC=70.00, ED=5.46, and total bill=320.

def calculate_electricity_bill(previous_reading, current_reading, customer_type):
    # Calculate the units consumed
    units_consumed = current_reading - previous_reading
    # Define rates based on customer type
    if customer_type == 'residential':
        rate_per_unit = 2.46  # Example rate for residential
        fixed_charge = 20.00
        customer_charge = 70.00
        energy_charge = units_consumed * rate_per_unit
        electricity_charge = energy_charge
        ed = electricity_charge * 0.0243  # Example ED calculation
    elif customer_type == 'commercial':
        rate_per_unit = 1.5  # Example rate for commercial
        fixed_charge = 50.00
        customer_charge = 100.00
        energy_charge = units_consumed * rate_per_unit
        electricity_charge = energy_charge
        ed = electricity_charge * 0.05  # Example ED calculation
    else:
        raise ValueError("Invalid customer type. Choose 'residential' or 'commercial'.")
    # Calculate total bill
    total_bill = electricity_charge + fixed_charge + customer_charge + ed
    # Print the bill components
    print(f"EC={electricity_charge:.2f}, FC={fixed_charge:.2f}, CC={customer_charge:.2f}, ED={ed:.2f}, Total Bill={total_bill:.2f}")
# Example usage
calculate_electricity_bill(2309, 2400, 'residential')
calculate_electricity_bill(2309, 2400, 'commercial')
