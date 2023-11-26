class Employee:
    def __init__(self, name, total_time_spent, dead_line):
        self.name = name
        self.total_time_spent = total_time_spent
        self.dead_line = dead_line

def calculate_efficiency(employee):
    time_ratio = min(1, employee.total_time_spent / employee.dead_line)

    baseline_efficiency = 50

    efficiency = baseline_efficiency + (1 - time_ratio) * 80 

    efficiency = min(efficiency, 100)

    return efficiency

def main():
    employee_name = input("Enter the employee's name: ")
    total_time_spent = float(input("Enter the total time spent (in hours): "))
    dead_line = float(input("Enter the task deadline (in hours): "))

    employee = Employee(employee_name, total_time_spent, dead_line)
    efficiency = calculate_efficiency(employee)

    if total_time_spent > dead_line:
        print("Efficiency: 20%")
       
    else:
        print(f"The efficiency of {employee_name} is: {efficiency}%")

if __name__ == "__main__":
    main()
