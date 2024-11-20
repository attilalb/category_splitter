import streamlit as st
import pandas as pd

def create_category_mapping():
    return {
        # Kitchen Products - Main Categories
        'papírszalvéta': 'Konyhai termékek|Papírszalvéták',
        'szalvéta': 'Konyhai termékek|Papírszalvéták',
        'kéztörlő': 'Konyhai termékek|Kéztörlők',
        'kitchen towel': 'Konyhai termékek|Kéztörlők',
        'kötény': 'Konyhai termékek|Kötények',
        'apron': 'Konyhai termékek|Kötények',
        'tál': 'Konyhai termékek|Tálak',
        'bowl': 'Konyhai termékek|Tálak',
        'tálca': 'Konyhai termékek|Tálalási kiegészítők',
        'serving': 'Konyhai termékek|Tálalási kiegészítők',
        'bögre': 'Konyhai termékek|Kancsók és csészék',
        'mug': 'Konyhai termékek|Kancsók és csészék',
        'cup': 'Konyhai termékek|Kancsók és csészék',
        'csésze': 'Konyhai termékek|Kancsók és csészék',
        'termosz': 'Konyhai termékek|Termoszok és termosz bögrék',
        'thermos': 'Konyhai termékek|Termoszok és termosz bögrék',
        'edényfogó kesztyű': 'Konyhai termékek|Sütőkesztyűk',
        'fémdoboz': 'Konyhai termékek|Ételdobozok',
        'lapostányér': 'Konyhai termékek|Tányérok',
        'desszerttányér': 'Konyhai termékek|Tányérok',
        'mélytányér': 'Konyhai termékek|Tányérok',
        'lapostányér': 'Konyhai termékek|Tányérok',
        'konyharuha': 'Konyhai termékek|Konyharuhák',

        
        # Home Decor
        'dekoráció': 'Lakás dekoráció|Fali dekorációk',
        'wall decor': 'Lakás dekoráció|Fali dekorációk',
        'gyertya': 'Lakás dekoráció|Gyertyák és mécsesek',
        'candle': 'Lakás dekoráció|Gyertyák és mécsesek',
        'mécses': 'Lakás dekoráció|Gyertyák és mécsesek',
        'gyufa': 'Lakás dekoráció|Gyertyák és mécsesek',
        'gyertyatartó': 'Lakás dekoráció|Gyertyatartók',
        'candleholder': 'Lakás dekoráció|Gyertyatartók',
        'illóolaj': 'Lakás dekoráció|Illóolajok és illatosítók',
        'aroma': 'Lakás dekoráció|Illóolajok és illatosítók',
        'képkeret': 'Lakás dekoráció|Képkeretek',
        'frame': 'Lakás dekoráció|Képkeretek',
        'kerti': 'Lakás dekoráció|Kerti dekorációk',
        'garden': 'Lakás dekoráció|Kerti dekorációk',
        'mágnes': 'Lakás dekoráció|Hűtőmágnesek',
        'magnet': 'Lakás dekoráció|Hűtőmágnesek',
        'ajtófogantyú': 'Lakás dekoráció|Ajtó gombok fogantyúk',
        'door handle': 'Lakás dekoráció|Ajtó gombok fogantyúk',
        'párna': 'Lakásdekoráció|Díszpárnák',
        'pillow': 'Lakásdekoráció|Díszpárnák',
        'figura': 'Lakás dekoráció|Dekorációs kiegészítők',
        'falifogas': 'Lakás dekoráció|Fogasok',
        
        # Artists
        'van gogh': 'Művészet|Vincent van Gogh',
        'klimt': 'Művészet|Gustav Klimt',
        'mucha': 'Művészet|Alfons Mucha',
        'monet': 'Művészet|Claude Monet',
        'botticelli': 'Művészet|Sandro Botticelli',
        'leonardo': 'Művészet|Leonardo Da Vinci',
        'frida kahlo': 'Művészet|Frida Kahlo',
        'beethoven': 'Művészet|Ludwig van Beethoven',
        
        # Seasonal
        'karácsony': 'Szezonális termékek|Karácsony',
        'christmas': 'Szezonális termékek|Karácsony',
        'függődísz': 'Szezonális termékek|Karácsony',
        'húsvét': 'Szezonális termékek|Húsvét',
        'easter': 'Szezonális termékek|Húsvét',
        'halloween': 'Szezonális termékek|Halloween',
        'valentin': 'Szezonális termékek|Esküvő, Valentin nap, Születésnap',
        'wedding': 'Szezonális termékek|Esküvő, Valentin nap, Születésnap',
        'születésnap': 'Szezonális termékek|Esküvő, Valentin nap, Születésnap',
        'birthday': 'Szezonális termékek|Esküvő, Valentin nap, Születésnap',
        'summer': 'Szezonális termékek|Summer&Beach',
        'beach': 'Szezonális termékek|Summer&Beach',
        'nyár': 'Szezonális termékek|Summer&Beach',
        'tenger': 'Szezonális termékek|Summer&Beach',
        'ősz': 'Szezonális termékek|Ősz',
        'autumn': 'Szezonális termékek|Ősz',
        'tavasz': 'Szezonális termékek|Tavasz',
        'spring': 'Szezonális termékek|Tavasz',
        
        # Themes
        'rózsa': 'Szezonális termékek|Rózsa',
        'rose': 'Szezonális termékek|Rózsa',
        'levendula': 'Szezonális termékek|Levendula',
        'lavender': 'Szezonális termékek|Levendula',
        'oliva': 'Gasztronómiai és Turisztikai boltoknak|Oliva',
        'tea': 'Gasztronómiai és Turisztikai boltoknak|Tea,Kávé',
        'coffee': 'Gasztronómiai és Turisztikai boltoknak|Tea,Kávé',
        
        # Animals
        'macska': 'Szezonális termékek|Imádom az állatokat',
        'cat': 'Szezonális termékek|Imádom az állatokat',
        'kutya': 'Szezonális termékek|Imádom az állatokat',
        'dog': 'Szezonális termékek|Imádom az állatokat',
        'bird': 'Szezonális termékek|Imádom az állatokat',
        'butterfly': 'Szezonális termékek|Imádom az állatokat',
        'horse': 'Szezonális termékek|Imádom az állatokat',
        'wild': 'Szezonális termékek|Imádom az állatokat',
        'pheasant': 'Szezonális termékek|Imádom az állatokat',
        'foxy': 'Szezonális termékek|Imádom az állatokat',
        'antlers': 'Szezonális termékek|Imádom az állatokat',

        # Cutlery
        'kés': 'Konyhai termékek|Evőeszközök',
        'kanál': 'Konyhai termékek|Evőeszközök',
        'villa': 'Konyhai termékek|Evőeszközök',
        'kiskanál': 'Konyhai termékek|Evőeszközök',
        'üvegpohár': 'Konyhai termékek|Poharak',
        'pohár': 'Konyhai termékek|Poharak',

        # Other
        'ajándéktáska': 'Szezonális termékek|Ajándék csomagolás',
        'csomagolópapír': 'Szezonális termékek|Ajándék csomagolás',
        'tányéralátét': 'Konyhai termékek|Tányéralátétek',
        'könyvjelző': 'Papír-írószer|Könyvjelzők',
        'zsebtükör': 'Divatkiegészítők|Kozmetikai tükör',
        'asztali futó': 'Konyhai termékek|Asztalterítők',
        'asztalterítő': 'Konyhai termékek|Asztalterítők',
        'pénztárca': 'Divatkiegészítők|Pénztárcák',


    }

def process_categories(df, category_mapping):
    def assign_category(product_name):
        product_name = str(product_name).lower()
        for keyword, category in category_mapping.items():
            if keyword.lower() in product_name:
                return category
        return None

    df['New_Category'] = df['Terméknév'].apply(assign_category)
    return df

st.title('Product Category Mapper')
st.write('Upload your product list CSV file to map categories')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV with proper encoding and separator
    df = pd.read_csv(uploaded_file, sep=';', encoding='utf-8')
    
    # Process categories
    category_mapping = create_category_mapping()
    result_df = process_categories(df, category_mapping)
    
    # Show results
    st.write("### Original Categories vs New Categories")
    comparison_df = result_df[['Terméknév', '1 category', 'New_Category']]
    st.dataframe(comparison_df)
    
    # Add download button
    csv = result_df.to_csv(sep=';', index=False, encoding='utf-8')
    st.download_button(
        label="Download processed CSV",
        data=csv,
        file_name="processed_categories.csv",
        mime="text/csv"
    )
    
    # Show statistics
    st.write("### Mapping Statistics")
    total_products = len(result_df)
    mapped_products = result_df['New_Category'].notna().sum()
    st.write(f"Total products: {total_products}")
    st.write(f"Successfully mapped: {mapped_products}")
    st.write(f"Mapping rate: {(mapped_products/total_products)*100:.2f}%")