import streamlit as st
import pandas as pd

def process_categories(df):
    def split_categories(text):
        if pd.isna(text) or ': >' not in text:
            return pd.Series([None] * 5)
        
        # Split by ': >' first
        main_parts = text.split(': >')
        if len(main_parts) < 2:
            return pd.Series([None] * 5)
            
        # First category is the left part (Kiemelt témák)
        first_category = main_parts[0].strip()
        
        # Process the remaining part
        remaining = main_parts[1].strip()
        
        # Handle different separators
        if ' -> ' in remaining:
            # Handle arrow separator
            categories = remaining.split(' -> ')
        else:
            # Handle comma separator
            categories = remaining.split(',')
        
        # Clean up categories
        categories = [cat.strip() for cat in categories]
        
        # Combine all categories starting with the first one
        all_categories = [first_category] + categories
        
        # Pad with None to ensure 5 columns
        all_categories.extend([None] * (5 - len(all_categories)))
        
        return pd.Series(all_categories[:5])

    # Process the categories
    category_cols = df['1 category'].apply(split_categories)
    category_cols.columns = ['Kategória 1', 'Kategória 2', 'Kategória 3', 'Kategória 4', 'Kategória 5']
    
    # Update the DataFrame
    result_df = df.copy()
    result_df[['Kategória 1', 'Kategória 2', 'Kategória 3', 'Kategória 4', 'Kategória 5']] = category_cols
    
    return result_df

st.title('Category Splitter')
st.write('Upload your CSV file to split the categories')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV with proper encoding and separator
    df = pd.read_csv(uploaded_file, sep=';', encoding='utf-8')
    
    # Process the file
    result_df = process_categories(df)
    
    # Show the results
    st.write("Processed Data:")
    st.dataframe(result_df)
    
    # Add download button
    csv = result_df.to_csv(sep=';', index=False, encoding='utf-8')
    st.download_button(
        label="Download processed CSV",
        data=csv,
        file_name="processed_categories.csv",
        mime="text/csv"
    )