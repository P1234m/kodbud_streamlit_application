
import streamlit as st
import random 
import os
from io import BytesIO
import zipfile
import re

st.sidebar.title("Navigation ")
page = st.sidebar.radio("Choose a Task", ["Home","About", "Simple Calculator", "Number Guessing Game", "File Renamer", "Password Strength Checker"])

if page == "Home":
    st.title("Kodbud Internship: Python Tasks Showcase")
    st.write("Welcome to my project showcase!")
    st.write("Please use the navigation on the left to select a task.")

    
elif page=="About":
    st.title("About Page")
    st.write("This page provides a brief overview of each task...")
    st.markdown("----")
    st.header("Task 1: Simple Command Line Calculator")
    st.markdown("""
    **Description:** This is a command-line calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.

    **Key Learnings:**
    - **Basic Python Syntax:** Reinforced my understanding of variables, data types (`float`, `str`), and operators.
    - **User Input/Output:** Practiced capturing user input with `input()` and displaying results with `print()`.
    - **Conditional Logic:** Used `if-elif-else` statements to control the program flow and perform the correct calculation.
    - **Streamlit Adaptation:** Learned to map command-line inputs to interactive widgets like `st.number_input` and `st.selectbox`.
    """)

    st.markdown("---")
    st.header("Task 2:Number guessing game")
    st.markdown("""
    **Description:** A classic game where the program thinks of a random number and the user has to guess it. The program provides hints like "Too high" or "Too low".

    **Key Learnings:**
    - **Random Module:** Used `random.randint()` to generate unpredictable numbers.
    - **Loops and State:** Implemented a `while` loop to continue the game until the correct guess was made.
    - **State Management in Streamlit:** This was a key challenge. I learned to use `st.session_state` to store variables (like the secret number and attempt count) across user interactions, which is essential for building stateful web apps.
    """)
    
    st.markdown("---")
    st.header("Task 4:File Renamer")
    st.markdown("""
    **Description:** The original task was to rename files in a local folder. For the web version, I adapted this to allow users to upload multiple files, which are then renamed sequentially and bundled into a downloadable `.zip` archive.

    **Key Learnings:**
    - **File Handling:** Gained experience with the `os` module for path and file extension manipulation.
    - **Web App Security & Functionality:** Understood that a web server cannot access a user's local file system. I learned to pivot the functionality to use `st.file_uploader`.
    - **In-Memory Operations:** Worked with `io.BytesIO` to create a file-like object in memory and the `zipfile` module to build a zip archive on the fly without saving it to the server's disk.
    """)

    st.markdown("---")
    st.header("Task 5:Password Strength Checker")
    st.markdown("""
    **Description:** This tool checks if a user-provided password meets certain criteria (minimum length, presence of numbers, uppercase letters, and special characters) and classifies it as "Strong" or "Weak".

    **Key Learnings:**
    - **String Manipulation:** Practiced checking the properties of strings.
    - **Regular Expressions (Regex):** Used the `re` module to search for specific patterns (like digits, uppercase letters, etc.) within the password string. This was a powerful tool for validation.
    - **Logical Grouping:** Combined multiple conditions to determine the final outcome, providing clear feedback to the user.
    """)
#Task 1
elif page == "Simple Calculator":
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:", value=0.0)
    operator = st.selectbox("Select an operation:", ('+', '-', '*', '/'))
    num2 = st.number_input("Enter the second number:", value=0.0)

    if st.button("Calculate"):
        result = 0.0
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/' and num2 != 0:
            result = num1 / num2
        elif num2 == 0:
            st.error("Error: Division by zero is not allowed.Enter different number.")
        
        if not (operator == '/' and num2 == 0):
             st.success(f"The result is: {result}")
    st.markdown("---")
    with st.expander("View the original Python code...."):
        st.code(
            '''print("Simple CLI Calculator")
num1=float(input("Enter first number: "))
operator=input("Enter operation (+,-,*,/): ")
num2=float(input("Enter second number: "))

#Performing the operation and returning the result

if operator=='+':
    print("Result: ",num1+num2)
elif operator=='-':
    print("Result: ",num1-num2)
elif operator=='*':
    print("Result: ",num1*num2)
elif operator=='/':
    print("Result: ",num1/num2)
else:
    print("Invalid operator")''',
    language='python'
        )
#Task 2
elif page == "Number Guessing Game":
    st.title("Number Guessing Game")

    # Initialize the game state if it doesn't exist
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.guess = 0
        st.session_state.game_over = False

    st.write("I'm thinking of a number between 1 and 100.")

    if not st.session_state.game_over:
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="user_guess")
        
        if st.button("Guess"):
            st.session_state.attempts += 1
            st.session_state.guess = guess
            
            if st.session_state.guess < st.session_state.secret_number:
                st.warning("Too low!")
            elif st.session_state.guess > st.session_state.secret_number:
                st.warning("Too high!")
            else:
                st.success(f"Perfect! You guessed it in {st.session_state.attempts} attempts.")
                st.balloons()
                st.session_state.game_over = True
    else:
        st.write(f"The number was {st.session_state.secret_number}. You guessed it!")


    if st.button("Play Again"):
        # Reset the game state
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.guess = 0
        st.session_state.game_over = False
        st.rerun()

    st.markdown("---")
    with st.expander("View original python code..."):
        st.code(
            '''import random
import time
def play_game():
    print("Welcome to the Number Guessing Game!")
    #choosing difficulty level to make the game more interesting
    difficulty=input("Choose difficulty (Easy/Medium/Hard): ")
    ranges={'easy':50,'medium':100,'hard':150}
    max_num=ranges.get(difficulty,100)
    #choosing the random number
    number=random.randint(1,max_num)
    attempts=0
    guess=[]
    start_time=time.time()
    print(f"I am trying to think of number between 1 to {max_num}!")
    print("Guess the number!")

    while True:
        try:
            input_number=int(input("Enter the guessed number..."))
            attempts+=1
            guess.append(input_number)

            if(input_number<number):
                print("Too Low!")
            elif(input_number>number):
                print("Too High!")
            elif(input_number==number):
                time_required=round(time.time()-start_time,2)
                print("Perfect Guess")
                print(f"You guessed in {time_required}s time and {attempts} attempts")
                print(f"your guesses : {guess}")
                break

        except ValueError:
            print("Please enter valid number...")
    if input("Play again: (yes/no)").lower()=='yes':
        play_game()

play_game()''',
language='python'
        )
    
#Task 4
elif page == "File Renamer":
    st.title("Automate File Renaming")
    
    st.write("Upload multiple files and I will rename them sequentially (file_1, file_2, etc.) and bundle them in a zip file for you to download.")

    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

    if uploaded_files:
        st.write(f"{len(uploaded_files)} files uploaded.")
        
        if st.button("Rename and Download"):
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
                for i, uploaded_file in enumerate(uploaded_files, start=1):
                    _, ext = os.path.splitext(uploaded_file.name)
                    new_filename = f"file_{i}{ext}"
                    zip_file.writestr(new_filename, uploaded_file.getvalue())

            st.download_button(
                label="Download Renamed Files as .zip",
                data=zip_buffer.getvalue(),
                file_name="renamed_files.zip",
                mime="application/zip"
            )

    st.markdown("---")
    with st.expander("View original python code..."):
        st.code(
            '''import os
#give folder path
folder_path="C:\\Users\\Dell\\example"
#list of all the files in the given folder
files=os.listdir(folder_path)

files.sort()

#iterate through the files to rename them

for index,file in enumerate(files,start=1):
    _,ext=os.path.splitext(file)
    new_file=f"file_{index}{ext}"
    old_path=os.path.join(folder_path,file)
    new_path=os.path.join(folder_path,new_file)
    os.rename(old_path,new_path)  #renaming

    print(f"{file} renamed to {new_file}")''',
    language="python"
        )

#Task 5
elif page == "Password Strength Checker":
    st.title("Password Strength Checker")
    
    password = st.text_input("Enter a password to check its strength:", type="password")

    if password:
        strength = "Weak"
        reasons = []

        if len(password) < 8:
            reasons.append("Must be at least 8 characters long.")
        else:
            reasons.append("Contains At least 8 characters long.")
        
        if not re.search(r"\d", password):
            reasons.append("Must contain at least one number.")
        else:
            reasons.append("Contains at least one number.")

        if not re.search(r"[A-Z]", password):
            reasons.append("Must contain at least one uppercase letter.")
        else:
            reasons.append("Contains at least one uppercase letter.")

        if not re.search(r"[!@#$^&*(),.%?\":{}|<>]", password):
            reasons.append("Must contain at least one special character.")
        else:
            reasons.append("Contains at least one special character.")

        # Check if all conditions are met
        if all("Contains" in reason for reason in reasons):
            strength = "Strong"
        
        st.write("---")
        if strength == "Strong":
            st.success("Password Strength: Strong")
        else:
            st.error("Password Strength: Weak")

        for reason in reasons:
            st.write(reason)
    st.markdown("---")
    with st.expander("View original python code..."):
        st.code(
            '''import re

def password_checker():
    password=input("Set password: ")

    #check the input password against provided rules and return whether "Weak" or "Strong"
    if len(password)<8:
        return "Weak"
    if not re.search(r"\d",password):
        return "Weak"
    if not re.search(r"[A-Z]",password):
        return "Weak"
    if not re.search(r"[!@#$^&*(),.%?\":{}|<>]",password):
        return "Weak"
    return "Strong"


#Call the function
while True: 
    strength=password_checker()
    if strength=="Strong":
        print("Password strength: Strong")
        break
    else :
        print("Password strength: Weak")
        print("Reset a strong password")''',
        language="python"
        )