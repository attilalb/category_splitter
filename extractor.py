import streamlit as st
import pandas as pd
import re

def extract_dimensions(name):
    # Find patterns like "22x9x23cm" or "33x33cm"
    match = re.search(r'(\d+)x(\d+)(?:x(\d+))?(?:cm)?', name)
    if match:
        dims = match.groups()
        if dims[2]:  # 3D dimensions (length x width x height)
            return int(dims[0]), int(dims[1]), int(dims[2])
        else:  # 2D dimensions (length x width)
            return int(dims[0]), int(dims[1]), None
    return None, None, None

def extract_volume(name):
    # Find patterns like "10db-os" or "20db-os"
    match = re.search(r'(\d+)db-os', name)
    return int(match.group(1)) if match else None

def process_product(row):
    name = row['Terméknév'].lower()
    
    # Extract color (simple word match)
    colors = ['white', 'green', 'black', 'cream', 'rose', 'blue', 'gold', 'fehér', 'fekete', 'piros', 'ezüst']
    color = next((c for c in colors if c in name), None)
    
    # Extract material
    materials = ['papír', 'műanyag', 'pamut', 'porcelán', 'fém', 'öntöttvas', 'textil']
    material = next((m for m in materials if m in name), None) 
    
    # Extract dimensions and volume
    length, width, height = extract_dimensions(name)
    volume = extract_volume(name)
    
    # Create size string if dimensions exist
    size = None
    if length and width:
        size = f"{length}x{width}{'x'+str(height) if height else ''}cm"
    
    return pd.Series({
        'Szín': color,
        'Anyag': material,
        'Méret': size,
        'Hosszúság': length,
        'Szélesség': width,
        'Magasság': height,
        'Űrtartalom': volume
    })

def main():
    st.title("Product Attribute Extractor")
    
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file:
        try:
            # Load data
            df = pd.read_csv(uploaded_file, sep=';', encoding='utf-8')
            
            # Process data
            with st.spinner('Processing products...'):
                results = df.apply(process_product, axis=1)
                df.update(results)
            
            # Display summary
            st.success(f"Processed {len(df)} products")
            
            # Filters
            st.sidebar.header("Filters")
            
            # Color filter
            available_colors = ['All'] + sorted([c for c in df['Szín'].dropna().unique() if c])
            color_filter = st.sidebar.selectbox('Color', available_colors)
            
            # Material filter
            available_materials = ['All'] + sorted([m for m in df['Anyag'].dropna().unique() if m])
            material_filter = st.sidebar.selectbox('Material', available_materials)
            
            # Apply filters
            filtered_df = df.copy()
            if color_filter != 'All':
                filtered_df = filtered_df[filtered_df['Szín'] == color_filter]
            if material_filter != 'All':
                filtered_df = filtered_df[filtered_df['Anyag'] == material_filter]
            
            # Display results
            st.subheader("Results")
            display_cols = ['Terméknév', 'Szín', 'Anyag', 'Méret', 'Hosszúság', 
                          'Szélesség', 'Magasság', 'Űrtartalom']
            st.dataframe(filtered_df[display_cols])
            
            # Download button
            csv = filtered_df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
            st.download_button(
                "Download Processed Data",
                csv,
                "processed_products.csv",
                "text/csv",
                key='download-csv'
            )
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()
