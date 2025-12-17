import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.agent import get_agent

def render_ui():
    st.title("📊 AI Data Agent (Team Project)")
    st.markdown("Цей агент вміє аналізувати дані та пояснювати терміни.")

    # Сайдбар
    with st.sidebar:
        st.header("Налаштування")
        api_key = st.text_input("Введи Groq API Key", type="password")
        uploaded_file = st.file_uploader("Завантаж CSV файл", type="csv")
        
        st.info("💡 Підказка: Спитай 'Яка ROI?' або 'Побудуй графік продажів'.")

    if uploaded_file and api_key:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("### Ваші дані:")
            st.dataframe(df.head(3))
            
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            agent = get_agent(df, api_key)

            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
                    
                    if "image_data" in msg: 
                        st.pyplot(msg["image_data"])

            if prompt := st.chat_input("Що зробити з даними?"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    with st.spinner("Думаю..."):
                        try:
                            
                            response = agent.invoke(prompt)
                            output_text = response["output"]
                            
                            st.markdown(output_text)
                            
                            
                            if plt.get_fignums():
                                st.pyplot(plt.gcf())
                                
                                st.session_state.messages.append({
                                    "role": "assistant", 
                                    "content": output_text,
                                    "image_data": plt.gcf()
                                })
                                plt.clf() 
                            else:
                                st.session_state.messages.append({
                                    "role": "assistant", 
                                    "content": output_text
                                })
                                
                        except Exception as e:
                            st.error(f"Помилка: {e}")

        except Exception as e:
            st.error(f"Не вдалося прочитати файл: {e}")