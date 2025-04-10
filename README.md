# Chat_bot - Personal Chatbot Web Application

## Project Overview
This project aims to develop an interactive personal chatbot that engages in real-time conversations and provides relevant responses based on user inputs. The chatbot is designed to simulate natural human-like conversations, making it an efficient and user-friendly solution for handling multiple user queries without requiring complex setups.

---

## Project Statement

### Purpose and Goals
In the era of Artificial Intelligence (AI), chatbots play a crucial role in automating user interactions. This project was chosen to develop a chatbot capable of efficiently handling user queries and delivering relevant responses using Bard AI API integrated into a web application built with Streamlit.

---

## Technical Stack
- Python
- Streamlit (Frontend Framework)
- Streamlit_chat (Chat Integration)
- Bard AI API (Conversational AI)

---

## Key Features
- Real-time Interactive Conversations
- Responsive Web Interface using Streamlit
- Bard AI API Integration for Human-like Responses
- Efficient Query Handling (100+ queries daily)
- Error Handling with Friendly Messages
- Chat History Management
- Option to Clear Chat History

---

## Implementation Workflow

### User Interaction Flow
1. User enters a query using Streamlit's input widget.
2. The input is sent to the Bard API using a secure token.
3. Bard API processes the input and returns a response.
4. The chatbot displays the response on the Streamlit interface.
5. Chat history is stored and displayed using the streamlit_chat library.

### Functions
- `generate_response(prompt)`: Sends user input to Bard API and retrieves response.
- `get_text()`: Captures user input.
- `on_btn_click()`: Clears the chat history for a new conversation.

---

## Challenges & Solutions

### API Response Time
- Challenge: Latency in API responses.
- Solution: 
  - Implemented caching for frequently asked questions.
  - Optimized API calls by reducing payload size.
  - Used asynchronous programming for non-blocking API requests.

### UI/UX Design
- Challenge: Creating a clean and intuitive interface.
- Solution: 
  - Focused on a minimalistic layout.
  - Incorporated user feedback for design improvements.

### Handling Diverse Inputs
- Challenge: Managing slang, misspellings, and complex queries.
- Solution: 
  - Implemented input normalization techniques.
  - Managed context for multi-turn conversations.
  - Used fallback responses for unclear inputs.

### Error Handling
- Quiet Error Handling using `try-except` blocks.
- Logged errors in the background for debugging.
- Provided generic user-friendly fallback responses.

---

## Future Enhancements
- Multi-language Support
- Advanced Context Management
- Graphical Representation of Data
- User Authentication for Personalized Experience
- Deployment to Cloud Platforms

---

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-repo/Chat_bot.git
```

2. Navigate to the project directory:
```bash
cd Chat_bot
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit Application:
```bash
streamlit run chatbot.py
```

---

## Outcome
This project provided hands-on experience in building interactive web applications, working with Natural Language Processing (NLP) APIs, and managing real-world challenges in API integration, UI/UX design, and error handling.




