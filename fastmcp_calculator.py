from fastmcp import FastMCP

mcp = FastMCP(name="Calculator")

@mcp.tool()
def multiply(a:float, b:float) -> float:
    """Multiplies two numbers.
    args:
        a (float): The first number.
        b (float): The second number.
    returns:
        float: The product of the two numbers
    """
    return a * b

@mcp.tool(name="divide",
            description="""Divides one number by another.
            args:
                a (float): The numerator.
                b (float): The denominator.
            returns:
                float: The result of the division.""",
            tags=["math", "division"])
def divide(a:float, b:float) -> float:
    """Divides one number by another.
    args:
        a (float): The numerator.
        b (float): The denominator.
    returns:
        float: The result of the division.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

@mcp.tool()
def add(a:float, b:float) -> float:
    """Adds two numbers.
    args:
        a (float): The first number.
        b (float): The second number.
    returns:
        float: The sum of the two numbers.
    """
    return a + b

@mcp.tool()
def subtract(a:float, b:float) -> float:
    """Subtracts one number from another.
    args:
        a (float): The number to subtract from.
        b (float): The number to subtract.
    returns:
        float: The result of the subtraction.
    """
    return a - b

if __name__ == "__main__":
    mcp.run() # Run the FastMCP application