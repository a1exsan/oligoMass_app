import streamlit as st

import oligoMass.molmassOligo as mmo

sequence = st.text_area('Enter sequence', '')
if st.button('analyse oligos') or sequence != '':
    st.write(f'Average mass: {round(mmo.oligoNASequence(sequence).getAvgMass(), 2)} Da')
    st.write(f'Monoisotopic mass: {round(mmo.oligoNASequence(sequence).getMonoMass(), 2)} Da')
    st.write(f'Molar extinction: {round(mmo.oligoNASequence(sequence).getExtinction(), 2)} OE/(mol ml)')

formula = st.text_area('Enter empirical formula', '')
if st.button('get mass') or formula != '':
    st.write(f'Average mass: {round(mmo.EmpericalFormula(formula).getAverageWeight(), 2)}, Da')
    st.write(f'Monoisotopic mass: {round(mmo.EmpericalFormula(formula).getMonoWeight(), 2)}, Da')
