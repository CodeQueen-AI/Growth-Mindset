import streamlit as st
import time

st.title("🚀 Find Your Coding Interest! 🤖")

name = st.text_input("👋 What's your name?", placeholder="Enter your name...")
experience = st.selectbox("🧠 Your coding experience level:", ["Beginner", "Intermediate", "Advanced"])
fav_lang = st.selectbox("💻 Favorite programming language:", ["Python", "JavaScript", "C++", "Java", "Other"])

progress = st.progress(0)

st.subheader("🎯 Let's understand your coding style!")

q1 = st.radio("🧩 Do you like solving **logical puzzles**?", ["Yes 🧠", "No ❌"])
q2 = st.radio("🐞 Do you enjoy **debugging** or **writing new code**?", ["Debugging 🕵️‍♂️", "Writing new code ✍️"])
q3 = st.radio("🎨 Do you prefer **designing user interfaces** or **working with data**?", ["UI/UX Design 🖌️", "Data Analysis 📊"])
q4 = st.radio("🤖 Are you interested in **AI and automation**?", ["Yes 🚀", "No ❌"])
q5 = st.radio("👨‍💻 Do you prefer working **alone** or **in a team**?", ["Solo Work 🏡", "Team Collaboration 🤝"])
q6 = st.radio("🧠 How do you solve problems?", ["Step-by-step planning 📜", "Trying different approaches 🔄"])
q7 = st.radio("🎮 Do you want to **create games**?", ["Yes 🎮", "No ❌"])
q8 = st.radio("💡 What excites you the most?", ["AI & Machine Learning 🤖", "Web Development 🌐", "Game Development 🎮", "Data Science 📊", "Cybersecurity 🔐", "Blockchain & Crypto 💎"])

interest = "Software Development 💻"  

if st.button("✨ Find My Coding Interest"):
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    if q8 == "AI & Machine Learning 🤖":
        interest = "Artificial Intelligence & Machine Learning 🤖"
    elif q8 == "Web Development 🌐":
        interest = "Front-end & Full-Stack Web Development 🌐"
    elif q8 == "Game Development 🎮":
        interest = "Game Development 🎮"
    elif q8 == "Data Science 📊":
        interest = "Data Science & Big Data 📊"
    elif q8 == "Cybersecurity 🔐":
        interest = "Ethical Hacking & Cybersecurity 🔐"
    elif q8 == "Blockchain & Crypto 💎":
        interest = "Blockchain Development & Crypto 🚀"
    elif q4 == "Yes 🚀":
        interest = "Artificial Intelligence & Automation 🤖"
    elif q3 == "UI/UX Design 🖌️":
        interest = "Front-end Web Development 🎨"
    elif q7 == "Yes 🎮":
        interest = "Game Development 🎮"
    elif q1 == "Yes 🧠":
        interest = "Competitive Programming & Algorithms 💡"
    else:
        interest = "Full Stack Development 🌐"

    st.balloons()
    st.success(f"🎉 Hey {name}, based on your answers, **you might enjoy {interest}!**")

    st.subheader("🔥 How to Get Started:")
    if interest == "Artificial Intelligence & Machine Learning 🤖":
        st.write("🔹 Start with Python, then explore libraries like TensorFlow & PyTorch.")
    elif interest == "Front-end & Full-Stack Web Development 🌐":
        st.write("🔹 Learn HTML, CSS, JavaScript, React.js, and Next.js.")
    elif interest == "Game Development 🎮":
        st.write("🔹 Try Unity (C#) or Unreal Engine (C++).")
    elif interest == "Data Science & Big Data 📊":
        st.write("🔹 Learn Python, Pandas, and visualization tools like Matplotlib & Seaborn.")
    elif interest == "Ethical Hacking & Cybersecurity 🔐":
        st.write("🔹 Learn about penetration testing, Kali Linux, and ethical hacking tools.")
    elif interest == "Blockchain Development & Crypto 🚀":
        st.write("🔹 Explore Solidity, Ethereum Smart Contracts, and Web3 technologies.")
    elif interest == "Competitive Programming & Algorithms 💡":
        st.write("🔹 Practice problems on LeetCode, Codeforces, and Hackerrank.")
    elif interest == "Full Stack Development 🌐":
        st.write("🔹 Learn both front-end (React, Next.js) and back-end (Node.js, MongoDB).")
