import streamlit as st

st.title("BMI 계산기")

height = st.number_input("키를 입력하세요 (cm)", min_value=0)
weight = st.number_input("몸무게를 입력하세요 (kg)", min_value=0)

if st.button("BMI 계산"):
    height_m = height / 100  # cm to m
    bmi = weight / (height_m ** 2)
    st.write(f"당신의 BMI는 {bmi:.2f}입니다.")  

    if bmi < 18.5:
        st.write("저체중입니다.")   

    elif 18.5 <= bmi < 24.9:
        st.write("정상 체중입니다.")
    
    elif 25 <= bmi < 29.9:
        st.write("과체중입니다.")
    else:
        st.write("비만입니다.")