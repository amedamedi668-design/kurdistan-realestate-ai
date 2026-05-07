import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# بيانات المشروع (يمكننا زيادتها لاحقاً)
data = {
    'area': [100, 150, 200, 120, 250, 100, 200, 150],
    'neighborhood': ['Bakhtiyari', 'Einkawa', 'Kasnazan', 'Bakhtiyari', 'Einkawa', 'Kasnazan', 'Bakhtiyari', 'Einkawa'],
    'age': [0, 5, 2, 10, 1, 15, 8, 4],
    'price': [95000, 130000, 190000, 65000, 240000, 45000, 160000, 145000]
}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['neighborhood'])
X = df_encoded.drop('price', axis=1)
y = df_encoded['price']

model = LinearRegression()
model.fit(X, y)

# تصميم الواجهة
st.set_page_config(page_title="Real Estate AI - Kurdistan", layout="centered")
st.title("🏡 نظام الذكاء الاصطناعي لتقدير العقارات")
st.subheader("مشروع خاص لمنطقة كردستان")

area = st.number_input("المساحة (متر مربع)", 50, 1000, 200)
age = st.slider("عمر البناء (بالسنوات)", 0, 50, 2)
location = st.selectbox("اختر الحي", ['Bakhtiyari', 'Einkawa', 'Kasnazan'])

if st.button("توقع السعر الآن"):
    # تجهيز البيانات للتنبؤ
    input_df = pd.DataFrame([[area, age, 0, 0, 0]], columns=X.columns)
    col_name = f'neighborhood_{location}'
    if col_name in input_df.columns:
        input_df[col_name] = 1
    
    res = model.predict(input_df)
    st.success(f"السعر التقديري هو: {res[0]:,.0f} دولار أمريكي")