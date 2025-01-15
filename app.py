import streamlit as st

from bmi_operations import calculate_bmi, bmi_to_remarks
st.header("BMI Calculator")

weight = st.text_input('Weight(in KG)',max_chars=10, 
                       placeholder='Enter your weight', value="60")

height = st.text_input('Height(in inches)',max_chars=4, 
                       placeholder='Enter your height', value="65")


if st.button('Calculate', help='Click here to calculate BMI',type='primary'):
    bmi = calculate_bmi(height, float(weight))
    bmi_remarks = bmi_to_remarks(bmi)

    st.status(f"Your BMI is {bmi}. Remarks: {bmi_remarks}", expanded=False, state="complete")


# Assignment
# Create any app you like 
# 2 constraint
# 1 It should atleast contain one new thing of streamlit
# 2 App should be user focused