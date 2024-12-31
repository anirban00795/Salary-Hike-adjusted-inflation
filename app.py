import streamlit as st

# Function to calculate the constant yearly hike percentage required to reach the future target salary
def calculate_constant_yoy_hike(target_salary_today, years_to_target, current_salary, inflation_rate=0.06):
    # Calculate the future target salary after inflation
    future_target_salary = target_salary_today * (1 + inflation_rate) ** years_to_target
    
    # Calculate the required constant YoY hike
    required_hike = ((future_target_salary / current_salary) ** (1 / years_to_target) - 1) * 100
    
    return required_hike, future_target_salary

# Streamlit UI
st.title('Year-on-Year Salary Hike Calculator (with Inflation)-Developed by Anirban Sengupta')

# Inputs for target salary, current salary, and inflation rate
target_salary_today = st.number_input("Enter your target salary today (equivalent to purchasing power)", min_value=0)
current_salary = st.number_input("Enter your current salary", min_value=0)
years_to_target = st.number_input("Enter the years until you reach the target salary (e.g., 8 years)", min_value=1)
inflation_rate = st.number_input("Enter the inflation rate (%) per year", min_value=0.0, step=0.01) / 100  # Convert percentage to decimal

# Calculate and display the required hike when button is pressed
if st.button('Calculate'):
    if target_salary_today and current_salary and years_to_target and inflation_rate >= 0:
        required_hike, future_target_salary = calculate_constant_yoy_hike(target_salary_today, years_to_target, current_salary, inflation_rate)
        
        st.write(f"Your target salary after {years_to_target} years, adjusted for inflation: ₹{future_target_salary:.2f}")
        st.write(f"The required Year-on-Year hike is: {required_hike:.2f}% each year.")
    else:
        st.error("Please fill in all fields.")
        
