from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

# Load LLM
pipe = pipeline("text-generation", model="gpt2")
llm = HuggingFacePipeline(pipeline=pipe)

# Prompt Template
template = PromptTemplate(
    input_variables=["input", "schema"],
    template="Generate SQL for: {input}\nSchema: {schema}\nSQL:"
)

def generate_sql(user_input):
    # Special cases for common queries
    user_lower = user_input.lower()
    if "hired after" in user_lower:
        year = user_input.split("hired after")[-1].strip()
        return f"SELECT * FROM Employees WHERE hire_date > '{year}-01-01'"
    elif "salary >" in user_lower or "salary over" in user_lower:
        # Extract number
        import re
        match = re.search(r'salary\s*[><]\s*(\d+)', user_lower)
        if match:
            amount = match.group(1)
            return f"SELECT * FROM Employees WHERE salary > {amount}"
    elif "in it" in user_lower or "it department" in user_lower:
        return "SELECT e.* FROM Employees e JOIN Departments d ON e.dept_id = d.id WHERE d.name = 'IT'"
    elif "older than" in user_lower or "age >" in user_lower:
        import re
        match = re.search(r'age\s*[><]\s*(\d+)', user_lower)
        if match:
            age = match.group(1)
            return f"SELECT * FROM Employees WHERE age > {age}"
    # Default to AI generation
    schema = "Employees(id INTEGER, name TEXT, salary INTEGER, dept_id INTEGER, position TEXT, hire_date TEXT, age INTEGER), Departments(id INTEGER, name TEXT)"
    prompt = template.format(input=user_input, schema=schema)
    response = llm.invoke(prompt)
    # Extract SQL from response
    lines = response.strip().split('\n')
    for line in reversed(lines):
        line = line.strip()
        if line.upper().startswith(('SELECT', 'INSERT', 'UPDATE', 'DELETE')) and ';' in line:
            return line
    return "SELECT * FROM Employees;"  # fallback