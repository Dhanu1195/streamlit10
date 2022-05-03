import streamlit as st
from review import reviewFilter


def main():
    st.title("Review Filter ")
    html_temp = """
        <div style="background-color:gray;padding:10px">
        <h2 style="color:white;text-align:center;">Review Filter</h2>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    file = st.file_uploader(label="Upload a csv")
    if st.button('predict'):
        df_filtered = reviewFilter(file)
        st.success("successfully filter the reviews")
        st.dataframe(data=df_filtered,width=800,height=800)

if __name__=='__main__':
    main()
