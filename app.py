# import streamlit as st
# from streamlit_js_eval import streamlit_js_eval
# import numpy as np
# from agent import DQNAgent

# st.set_page_config(layout="wide")

# # Predefined search options
# # ["What is RL?", "TensorFlow tutorial", "Weather today", "News headlines", "Python examples"]
# search_options = st.text_input("Search Options", value="")

# state_size = 3  # simulate state as last 3 chosen options
# action_size = len(search_options)

# # Initialize session state
# if 'agent' not in st.session_state:
#     st.session_state.agent = DQNAgent(state_size, action_size)
# if 'state_history' not in st.session_state:
#     st.session_state.state_history = [0, 0, 0]  # dummy init
# if 'current_action' not in st.session_state:
#     st.session_state.current_action = None

# # Agent chooses action
# state = np.array(st.session_state.state_history[-3:])
# action = st.session_state.agent.act(state)
# search_query = search_options[action]

# # Show in iframe via Bing workaround
# url = f"https://www.bing.com/search?q={search_query.replace(' ', '+')}"
# st.markdown(f"### RL Agent Search: `{search_query}`")
# st.markdown(f'<iframe src="{url}" width="100%" height="500px"></iframe>', unsafe_allow_html=True)

# # Capture user reward via keyboard
# key = streamlit_js_eval(js_expressions="window.onkeydown = (e) => e.key;", key="reward_key")
# reward = 0
# if key == "y":
#     reward = 1
# elif key == "n":
#     reward = -1

# # Update RL agent
# if reward != 0:
#     next_state = st.session_state.state_history[-2:] + [action]
#     st.session_state.agent.remember(state, action, reward, next_state)
#     st.session_state.agent.replay()
#     st.session_state.state_history.append(action)
#     st.success(f"Reward `{reward}` received. Agent trained.")
# else:
#     st.info("Press `y` for good result or `n` for bad result to give reward.")



import streamlit as st
import numpy as np
from agent import DQNAgent

st.set_page_config(layout="wide")

# Input field for the user
user_input = st.text_input("Enter a search query:")

if user_input != "":
    search_options = [user_input]
else:
    # Predefined search options
    search_options = ["What is RL?", "TensorFlow tutorial", "Weather today", "News headlines", "Python examples"]

state_size = 3  # simulate state as last 3 chosen options
action_size = len(search_options)

# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = DQNAgent(state_size, action_size)
if 'state_history' not in st.session_state:
    st.session_state.state_history = [0, 0, 0]  # dummy init
if 'current_action' not in st.session_state:
    st.session_state.current_action = None

# Button to execute the RL agent after text input
if st.button("Run RL Agent"):
    if user_input:
        # Agent chooses action based on state
        state = np.array(st.session_state.state_history[-3:])
        action = st.session_state.agent.act(state)

        # Ensure the action is within bounds of search_options
        action = action % len(search_options)  # Modulo operation to wrap action within range

        search_query = search_options[action]

        # Show the search result iframe via Bing workaround
        url = f"https://www.bing.com/search?q={search_query.replace(' ', '+')}"
        st.markdown(f"### RL Agent Search: `{search_query}`")
        st.markdown(f'<iframe src="{url}" width="100%" height="500px"></iframe>', unsafe_allow_html=True)

        # Reward buttons
        reward = None  # Initialize reward

        if st.button("Good result +1"):
            reward = 1  # Set reward to 1 if "Good result" button is clicked
        if st.button("Bad result -1"):
            reward = -1  # Set reward to -1 if "Bad result" button is clicked

        # If a reward is given, update the RL agent
        if reward is not None:
            next_state = st.session_state.state_history[-2:] + [action]
            st.session_state.agent.remember(state, action, reward, next_state)
            st.session_state.agent.replay()
            st.session_state.state_history.append(action)

            if reward == 1:
                st.success("Good result received. Agent trained!")
            elif reward == -1:
                st.error("Bad result received. Agent trained!")
    else:
        st.warning("Please enter a search query to proceed.")
