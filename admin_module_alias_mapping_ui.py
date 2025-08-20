# admin_module_alias_mapping_ui.py
# Streamlit-UI zur Pflege der Spaltenalias-Konfiguration für den PDF-Importer
from __future__ import annotations
import streamlit as st

from database import load_admin_setting, save_admin_setting

st.set_page_config(page_title="Alias-Mapping (Modul-PDF)", layout="centered")
st.title("Alias-Mapping für Modul-PDF Import")

st.markdown("Hinterlege hier Abbildungsregeln: Spaltenname in der PDF -> kanonischer Key (z. B. cell_technology).")
st.caption("Der Importer normalisiert PDF-Header zu lowercase und reduziert Whitespaces. Trage deine Varianten hier ein.")

current = load_admin_setting("module_pdf_alias_map", {}) or {}

st.subheader("Aktuelle Aliase")
if not current:
    st.info("Noch keine Aliase gesetzt.")
else:
    for k, v in current.items():
        st.write(f"• '{k}' → '{v}'")

st.markdown("---")
st.subheader("Alias hinzufügen/ändern")
with st.form("alias_form"):
    col1, col2 = st.columns(2)
    with col1:
        src = st.text_input("PDF-Spaltenname (Variante)")
    with col2:
        dst = st.text_input("Kanonischer Key", help="z. B. cell_technology, module_structure, cell_type, version, model_name, brand, capacity_w ...")
    ok = st.form_submit_button("Speichern")
    if ok:
        if not src or not dst:
            st.error("Beide Felder erforderlich.")
        else:
            current[src] = dst
            if save_admin_setting("module_pdf_alias_map", current):
                st.success("Gespeichert.")
                st.experimental_rerun()
            else:
                st.error("Konnte nicht speichern.")

st.markdown("---")
st.subheader("Alias löschen")
del_key = st.text_input("PDF-Spaltenname zum Löschen", value="")
if st.button("Löschen"):
    if del_key in current:
        current.pop(del_key)
        if save_admin_setting("module_pdf_alias_map", current):
            st.success("Gelöscht.")
            st.experimental_rerun()
        else:
            st.error("Konnte nicht speichern.")
    else:
        st.warning("Nicht gefunden.")
