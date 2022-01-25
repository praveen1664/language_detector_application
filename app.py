import pickle
import streamlit as st
import sklearn

st.set_page_config(
    page_title="Languagedetector",
    layout="wide",
    initial_sidebar_state="expanded"
)

max_width_str = f"max-width: 1600px;"
st.markdown(
	f"""
		<style>
			.reportview-container .main .block-container {{{max_width_str}}}
		</style>    
	""",
	unsafe_allow_html=True
)

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    LanguageDetectFile=open("model.pckl",'rb')
    LanguageDetectModel=pickle.load(LanguageDetectFile)
    LanguageDetectFile.close()
    st.info("Welcome to Language Detection Tool")

    input_test=st.text_input("Enter your text input here & press below button","Input (Any language)")
    button_clicked=st.button("Get Language name")
    if button_clicked:
        st.text(LanguageDetectModel.predict([input_test]))

    hide_menu_style="""
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
    """
    st.markdown(hide_menu_style,unsafe_allow_html=True)  


try:
    if __name__=='__main__':
        main()
except Exception as e:
    print(f"We face the Error \n {e}")