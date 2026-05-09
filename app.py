import streamlit as st
from model import generate_sql
from database import run_query, create_db

# Create DB
create_db()

# Page config
st.set_page_config(
    page_title="AI SQL Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.header("📊 About")
    st.markdown("""
    This AI-powered SQL Agent converts natural language queries into SQL and executes them against a sample employee database.
    
    **Database Schema:**
    - **Employees**: id, name, salary, dept_id, position, hire_date, age
    - **Departments**: id, name
    
    **Try queries like:**
    - Show all employees
    - Find employees in IT department
    - List employees hired after 2020
    - Show average salary by department
    - Find employees older than 30
    """)
    st.markdown("---")
    st.markdown("Built with Streamlit & GPT-2")

# Main content
st.title("🤖 AI SQL Agent")
st.markdown("### Enter your query in natural language:")

# Input section
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.write("**Query:**")
with col2:
    user_input = st.text_input("", placeholder="e.g., Show me all employees with salary over 50000", label_visibility="collapsed")
with col3:
    run_button = st.button("🚀 Run Query", type="primary", use_container_width=True)

if run_button and user_input:
    with st.spinner("Generating SQL and querying database..."):
        sql_query = generate_sql(user_input)
    
    # SQL Display
    st.success("✅ SQL Generated Successfully!")
    st.code(sql_query, language="sql")
    
    # Results
    st.markdown("### 📋 Query Results")
    try:
        result = run_query(sql_query)
        if result:
            st.table(result)
            st.info(f"Found {len(result)} result(s)")
        else:
            st.warning("No results found for this query.")
    except Exception as e:
        st.error("❌ Error executing SQL")
        st.write(f"**Error details:** {str(e)}")
        st.markdown("*Try simplifying your query or check the SQL syntax.*")