import streamlit as st
import numpy as np
import pandas as pd

def home_page():
    st.markdown("Home page")
    st.sidebar.markdown("Home page")

    st.write("""
    The aim of this app is to process and plot a vibrational spectroscopy spectrum\n
    \n
    Index:\n
        Page 1: Cosmic Ray Removal\n
    """)


def page1():
    st.markdown("Page 1: Cosmic ray removal")
    st.sidebar.markdown("Page 1: Cosmic ray removal")
    
    st.write('''This page is to remove the cosmic rays from the spectra in the dataset''')

    cosmic_ray_remove_df = st.file_uploader('Upload file', type=['csv'])

    if cosmic_ray_remove_df is not None:
        crr_df = pd.read_csv(cosmic_ray_remove_df)

        if not crr_df.empty:

            def find_cosmic_rays(spectrum):
                """Finds cosmic rays in a spectrum using sigma-clipping."""
                n = len(spectrum)
                spectrum_clean = np.copy(spectrum)
                flagged_indices = []
    
                window_size = 25
    
                for i in range(window_size // 2, n - window_size // 2):
                    sigma = 3.0
                    window = spectrum[i - window_size // 2: i + window_size // 2 + 1]
                    mean = np.mean(window)
                    std = np.std(window)
        
                    if np.abs(spectrum[i] - mean) > sigma * std:
                        flagged_indices.append(i)
                        spectrum_clean[i] = mean
            
                return spectrum_clean
    

            def apply_function_recursive(vector):
                """Applies a function recursively until the vector and func(vector) are the same"""
                if np.allclose(find_cosmic_rays(vector), vector):
                    return vector
                else:
                    result = find_cosmic_rays(vector)
                    return apply_function_recursive(result)
            
            cosmic_ray_removed = np.apply_along_axis(apply_function_recursive, 1, crr_df.values)
            df_cr = pd.DataFrame(cosmic_ray_removed)

            st.write('Cosmic rays removed!')

            if st.button('Save as CSV'):
                # Save the DataFrame as a CSV file
                df_cr.to_csv('data_crr.csv', index=False)
                st.success('CSV file saved successfully.')


page_names_to_funcs = {  
    "Home Page": home_page,
    "Page 1 (Cosmic Ray Removal)": page1,
}

selected_page = st.sidebar.selectbox("Select a page", list(page_names_to_funcs.keys()))
page_names_to_funcs[selected_page]()