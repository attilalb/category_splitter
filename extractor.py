import streamlit as st
import pandas as pd
import re

def extract_dimensions(name):
    # Replace comma with dot for decimal numbers
    name = name.replace(',', '.')
    
    # Try to find 2D or 3D dimensions first (e.g., "22,5x9x23cm" or "33,5x33cm")
    multi_dim = re.search(r'(\d+\.?\d*)x(\d+\.?\d*)(?:x(\d+\.?\d*))?(?:cm)?', name)
    
    # Try to find single dimension (e.g., "15cm", "11cm")
    single_dim = re.search(r'(?<!\d)(\d+\.?\d*)(?:\s)?cm(?!\s*x)', name)
    
    def format_number(num_str):
        if num_str:
            num = float(num_str)
            return f"{int(num) if num.is_integer() else num}cm"
        return None
    
    if multi_dim:
        dims = multi_dim.groups()
        if dims[2]:  # 3D dimensions
            return format_number(dims[0]), format_number(dims[1]), format_number(dims[2])
        else:  # 2D dimensions
            return format_number(dims[0]), format_number(dims[1]), None
    elif single_dim:  # Single dimension
        return None, None, None, format_number(single_dim.group(1))
    
    return None, None, None, None

def extract_volume(name):
    ml_match = re.search(r'(\d+)ml', name)
    l_match = re.search(r'(\d+\,?\d*)l', name)
    
    if ml_match:
        return f"{ml_match.group(1)}ml"
    elif l_match:
        return f"{l_match.group(1)}l"
    return None

def process_product(row):
    name = row['Terméknév'].lower()
    
    # Extract color (simple word match)
    colors = ['white', 'green', 'black', 'cream', 'rose', 'blue', 'gold', 'fehér', 'fekete', 'piros', 'ezüst', 'arany', 'bézs', 'kék', 'sárga', 'zöld', 'barna']
    color = next((c for c in colors if c in name), None)
    
    # Extract material
    materials = ['papír', 'műanyag', 'pamut', 'porcelán', 'fém', 'öntöttvas', 'textil', 'kerámia', 'műbőr', 'polyester', 'üveg', 'vászon', 'alumínium']
    material = next((m for m in materials if m in name), None) 
    
    # Extract dimensions and volume
    dims = extract_dimensions(name)
    if len(dims) == 4:  # Single dimension found
        length, width, height, single_size = dims
    else:  # Multi dimensions or no dimensions
        length, width, height = dims
        single_size = None
        
    volume = extract_volume(name)
    
    # Create size string
    size = None
    if length and width:
        size = f"{length.replace('cm', '')}x{width.replace('cm', '')}{'x'+height.replace('cm', '') if height else ''}cm"
    elif single_size:
        size = single_size
    

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
