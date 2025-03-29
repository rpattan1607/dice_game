import streamlit as st
import random
import time

# Apply custom CSS for a modern, production-quality design
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        h1 {
            color: #f8f9fa;
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            margin-top: 20px;
        }
        p {
            color: #f8f9fa;
            text-align: center;
            font-size: 1.3em;
            margin-bottom: 20px;
        }
        .stButton > button {
            background-color: #ff9800 !important;
            color: white !important;
            border: none !important;
            padding: 12px 24px;
            font-size: 1.3em;
            border-radius: 12px;
            display: block;
            margin: 20px auto;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #e68900 !important;
        }
        .dice-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 150px;
            margin-top: 30px;
        }
        .result-box {
            text-align: center;
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            border-radius: 10px;
            font-size: 1.5em;
            font-weight: bold;
            margin-top: 20px;
        }
        .dice-img {
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# List of restaurants
restaurants = ["Pizza 4P's Indiranagar", "The Pizza Bakery", "Burger Joint", "Pasta House", "Taco Truck", "Indian Delight"]

dice_images = {
    1: "https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png",
    2: "https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png",
    3: "https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png",
    4: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png",
    5: "https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png",
    6: "https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png"
}

def roll_dice():
    return random.randint(1, 6)

def animate_dice(final_roll, placeholder):
    for _ in range(10):  # Simulate rolling effect
        placeholder.markdown(f'''
            <div class="dice-container">
                <img src="{random.choice(list(dice_images.values()))}" width="120">
            </div>
        ''', unsafe_allow_html=True)
        time.sleep(0.1)
    
    placeholder.markdown(f'''
        <div class="dice-container">
            <img src="{dice_images[final_roll]}" width="120">
        </div>
    ''', unsafe_allow_html=True)

def main():
    st.markdown("""
        <h1>Dice Rotater - Restaurant Chooser</h1>
        <p>Roll the dice three times to pick a restaurant!</p>
    """, unsafe_allow_html=True)
    
    if 'rolls' not in st.session_state:
        st.session_state.rolls = []
    
    if 'current_roll' not in st.session_state:
        st.session_state.current_roll = None
    
    dice_placeholder = st.empty()
    
    if st.button("Roll the Dice"):
        if len(st.session_state.rolls) < 3:
            roll = roll_dice()
            animate_dice(roll, dice_placeholder)
            st.session_state.rolls.append(roll)
            st.session_state.current_roll = roll
    
    st.write("Rolls so far:", st.session_state.rolls)
    
    if len(st.session_state.rolls) == 3:
        chosen_restaurant = restaurants[sum(st.session_state.rolls) % len(restaurants)]
        st.markdown(f'<div class="result-box">Your restaurant is: {chosen_restaurant}!</div>', unsafe_allow_html=True)
        
        if st.button("Reset"):
            st.session_state.rolls = []
            st.session_state.current_roll = None

if __name__ == "__main__":
    main()
