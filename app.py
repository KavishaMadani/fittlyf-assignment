import streamlit as st
from scipy.stats import norm

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors
    diff = treatment_rate - control_rate
    se = (control_rate * (1 - control_rate) / control_visitors + treatment_rate * (1 - treatment_rate) / treatment_visitors)**0.5
    z = diff / se
    if confidence_level == 90:
        if z > 1.645:
            return "Experiment Group is Better"
        elif z < -1.645:
            return "Control Group is Better"
        else:
            return "Indeterminate"
    elif confidence_level == 95:
        if z > 1.96:
            return "Experiment Group is Better"
        elif z < -1.96:
            return "Control Group is Better"
        else:
            return "Indeterminate"
    elif confidence_level == 99:
        if z > 2.576:
            return "Experiment Group is Better"
        elif z < -2.576:
            return "Control Group is Better"
        else:
            return "Indeterminate"

def main():
    st.title('A/B Test Hypothesis Testing App')
    st.sidebar.header('Input Parameters')
    control_visitors = st.sidebar.number_input('Control Group Visitors', min_value=1, step=1)
    control_conversions = st.sidebar.number_input('Control Group Conversions', min_value=0, step=1)
    treatment_visitors = st.sidebar.number_input('Treatment Group Visitors', min_value=1, step=1)
    treatment_conversions = st.sidebar.number_input('Treatment Group Conversions', min_value=0, step=1)
    confidence_level = st.sidebar.selectbox('Confidence Level', [90, 95, 99])
    if st.sidebar.button('Run Test'):
        result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.write(f"AB Test Result: {result}")

if __name__ == '__main__':
    main()
