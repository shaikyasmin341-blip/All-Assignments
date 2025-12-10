#Task Description #3 – Optimization
#Task: Write python code to solve below case study using linear optimization
"""Here is the **case study rewritten in clean sentence format**, ready to **copy and paste** anywhere:

---

### ✅ **Case Study (Copy-Paste Version)**"""

"""Consider a chocolate manufacturing company that produces two types of chocolates: A and B. Both chocolates require only two ingredients — Milk and Choco.

To manufacture each unit of Chocolate A and Chocolate B, the following quantities are required:

* Each unit of A requires 1 unit of Milk and 3 units of Choco.
* Each unit of B requires 1 unit of Milk and 2 units of Choco.

The company has a total of 5 units of Milk and 12 units of Choco available in its kitchen.

On selling, the company earns a profit of Rs. 6 per unit of Chocolate A and Rs. 5 per unit of Chocolate B.

The company's goal is to **maximize profit**.
**How many units of A and B should it produce respectively to achieve maximum profit?**"""

from scipy.optimize import linprog
# Coefficients for the objective function (negative for maximization)
c = [-6, -5]  # Profit per unit of A and B
# Coefficients for the inequality constraints
A = [
    [1, 1],   # Milk constraint
    [3, 2]    # Choco constraint
]
# Right-hand side of the inequality constraints
b = [5, 12]  # Available units of Milk and Choco
# Bounds for each variable (units of A and B cannot be negative)
x0_bounds = (0, None)  # Bounds for Chocolate A
x1_bounds = (0, None)  # Bounds for Chocolate B
# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
# Output the results
if res.success:
    print(f"Optimal number of units to produce:")
    print(f"Chocolate A: {res.x[0]:.2f} units")
    print(f"Chocolate B: {res.x[1]:.2f} units")
    print(f"Maximum Profit: Rs. {-res.fun:.2f}")
else:
    print("No solution found.")