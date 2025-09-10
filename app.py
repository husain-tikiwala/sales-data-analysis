import streamlit as st
import random as rd

st.title=("rock,paper and scissors game")#this is to give a title or heading to website

user_input = st.selectbox("choose your preference:",["rock","paper","scissors"])#selectbox is a function to make drop down list of choices in the list 

computer_choice = rd.choice(["rock","paper","scissors"])#to make randomly choose systemany from given in the list of rd.choice

if st.button("play"):#it shows a button play to execute function
    st.write("your chice is:",user_input)#write is just similar toprint function as it shows the user choice you opt for
    st.write("computer choice is :",computer_choice)
    if user_input == computer_choice:
        st.write("Result: It's a Tie!")
    elif (
    (user_input == "rock" and computer_choice == "scissors") or
    (user_input == "paper" and computer_choice == "rock") or
    (user_input == "scissors" and computer_choice == "paper")
    ):
        st.success("Result: You Win!")
        
        st.balloons()
    else:
        st.error("Result: You Lose!")
        st.snow()