# pip install FastMCP to install FastMCP
from fastmcp import FastMCP
import json

mcp = FastMCP("HRPilot")


with open("employees.json") as f:
    employees = json.load(f)

with open("leavebalances.json") as f:
    leavebalances = json.load(f)


@mcp.tool()
def get_employee(employee_id: str):
    """Get employee details"""

    return employees.get(
        employee_id,
        {"error": "Employee not found"}
    )


@mcp.tool()
def get_leave_balance(employee_id: str):
    """Get leave balance"""

    return leavebalances.get(
        employee_id,
        {"error": "Leave data not found"}
    )


if __name__ == "__main__":
    mcp.run()