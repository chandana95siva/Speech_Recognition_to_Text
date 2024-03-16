import streamlit as st
import speech_recognition as sr
from googletrans import Translator

def transcribe_and_translate(language, translate_to):
    listener = sr.Recognizer()
    translator = Translator()
    with sr.Microphone() as source:
        st.sidebar.subheader(f"Listening in {language}...")
        st.write("Click the button below to start recording:")
        recording_button = st.button("Start Recording")
        if recording_button:
            with st.spinner('Recording...'):
                audio = listener.listen(source)
            st.success('Audio captured!')

            try:
                if language == "Tamil":
                    text = listener.recognize_google(audio, language="ta-IN")
                elif language == "English":
                    text = listener.recognize_google(audio, language="en-US")
                else:
                    text = listener.recognize_google(audio, language="en-US")  # Default to English

                st.write("You said:", text)

                # Translate to the required language
                translated_text = translator.translate(text, dest=translate_to)
                st.write("Translated:", translated_text.text)
                st.success("Tranlated successfully!")

            except sr.UnknownValueError:
                st.error("Could not understand audio")
            except sr.RequestError as e:
                st.error(f"Error: {e}")

def main():
    st.title("Speech-to-Text and Translation App")
    
    st.image("speech.jpg", caption="Speech Recognition and Translation", use_column_width=True)
    
    st.sidebar.title("Options")
    language = st.sidebar.selectbox("Select Language", ["Tamil", "English"])
    translate_to = st.sidebar.selectbox("Translate to", ["English", "Tamil"])  
    transcribe_and_translate(language, translate_to)

if __name__ == "__main__":
    main()
