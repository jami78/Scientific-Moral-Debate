import streamlit as st
import requests

API_URL = "http://localhost:8000/run_debate" 

# Map agent names to emojis
AGENT_EMOJIS = {
    "Neuroscience": "🧠",
    "Psychology": "🗣️",   
    "Sociology": "🏛️",
    "EvoBio": "🐒", 
    "Arbiter": "⚖️"
}

st.title("🧭 AI Moral Debate System")
st.subheader("Ask a moral question and let scientists debate!")

# Input field
moral_question = st.text_area("Enter a moral dilemma/question:", height=100)

if st.button("Start Debate") and moral_question.strip():
    with st.spinner("Running multi-agent debate..."):
        try:
            response = requests.post(API_URL, json={"input": moral_question})
            data = response.json()

            if "messages" in data:
                st.success("Debate completed. See outputs below:")

                for msg in data["messages"]:
                    agent_name = msg["name"].replace(" ", "") 
                    emoji = AGENT_EMOJIS.get(agent_name, "🤖")
                    st.markdown(f"### {emoji} {msg['name']} [{msg['step'].capitalize()}]")
                    st.markdown(msg["content"])
                    st.markdown("---")

                st.markdown("## ⚖️ Final Conclusion")
                st.markdown(data["final_conclusion"])

            else:
                st.error("Unexpected response format from server.")

        except Exception as e:
            st.error(f"Error occurred: {e}")
else:
    st.info("Enter a question and click 'Start Debate' to begin.")
