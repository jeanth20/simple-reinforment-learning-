# RL Search Agent

A Streamlit-based web application that implements a Reinforcement Learning (RL) agent to improve search queries based on user feedback.

## Overview

This application uses a Deep Q-Network (DQN) agent to learn from user interactions and optimize search results. The agent adapts its search strategy based on positive or negative feedback provided by users.

## Features

- Interactive search interface
- Real-time search results display using Bing search
- Reinforcement Learning agent that learns from user feedback
- Custom search query input
- Predefined search options for quick testing
- Visual feedback for agent training

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rl-search-agent
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install streamlit numpy streamlit-js-eval
```

## Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## How to Use

1. **Enter a Search Query**:
   - Type your search query in the text input field, or
   - Use the predefined search options

2. **Execute Search**:
   - Click the "Run RL Agent" button to perform the search

3. **Provide Feedback**:
   - Click "Good result +1" if the search result was helpful
   - Click "Bad result -1" if the search result was not helpful

4. **View Results**:
   - The search results will be displayed in an embedded iframe
   - The agent will learn from your feedback and improve future searches

## Project Structure

```
.
├── app.py          # Main Streamlit application
├── agent.py        # DQN Agent implementation
└── README.md       # Project documentation
```

## Technical Details

- **Framework**: Streamlit
- **RL Implementation**: Deep Q-Network (DQN)
- **State Space**: Last 3 chosen search options
- **Action Space**: Available search queries
- **Reward System**: Binary feedback (+1 for good, -1 for bad results)

## Limitations

- Search results are limited to Bing search engine
- The agent's learning is session-based and resets when the application restarts
- Iframe restrictions may affect some search result displays

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

Apache 2.0

