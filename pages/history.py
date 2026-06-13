import streamlit as st
import pandas as pd

from database.db import get_all_analyses

st.title("📜 Analysis History")

data = get_all_analyses()

if data:

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info(
        "No analyses found."
    )