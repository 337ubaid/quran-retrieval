import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query 

# # Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = execute_query(conn.table("ayat_quran").select("*"), ttl=None)

# Print results.
for row in rows.data:
    st.write(f"{row['id']} : {row['indoText']}:")