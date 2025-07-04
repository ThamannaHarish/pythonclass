import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 CSV Plot Viewer (Tips Dataset Example)")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Histogram of total_bill
    axs[0, 0].hist(df['total_bill'], bins=15, color='skyblue', edgecolor='black')
    axs[0, 0].set_title("Histogram of Total Bill")

    # Boxplot of tip
    axs[0, 1].boxplot(df['tip'], patch_artist=True)
    axs[0, 1].set_title("Boxplot of Tips")

    # Pie chart of gender distribution
    gender_counts = df['sex'].value_counts()
    axs[1, 0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    axs[1, 0].set_title("Gender Distribution")

    # Bar chart of average total bill by day
    avg = df.groupby("day")["total_bill"].mean()
    axs[1, 1].bar(avg.index, avg.values, color='lightgreen')
    axs[1, 1].set_title("Avg Total Bill by Day")

    st.pyplot(fig)
