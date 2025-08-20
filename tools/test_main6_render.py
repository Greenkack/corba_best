import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so imports from parent work
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pdf_generator as pg

project_data = {
    'customer_data': {
        'salutation': 'Herr',
        'title': '',
        'first_name': 'Max',
        'last_name': 'Mustermann',
        'address': 'Musterweg',
        'house_number': '12',
        'zip_code': '12345',
        'city': 'Musterstadt',
        'phone_mobile': '+491234567',
        'email': 'max@example.com'
    },
    'project_details': {
        # Trigger headings and dynamic title values
        'module_quantity': 20,
        'selected_module_capacity_w': 420,
        # Provide explicit module extended fields to verify mapping
        'module_manufacturer': 'JA Solar',
        'module_model': 'JAM54S31-420/MR',
        'module_cell_technology': 'Monokristallin N-Type',
        'module_structure': 'Glas-Folie',
        'module_cell_type': '108 Halbzellen',
        'module_version': 'Black Frame',
        'module_guarantee_combined': '25 Jahre Produktgarantie | 30 Jahre Leistungsgarantie',

        # Inverter fields
        'selected_inverter_name': 'Huawei SUN2000-8KTL-M1',
        'selected_inverter_quantity': 1,
        'selected_inverter_power_kw': 8,

        # Storage to trigger Huawei LUNA specifics
        'selected_storage_name': 'Huawei LUNA2000-7-S1-7kWh Stromspeicher',
        'include_storage': True,
    }
}
analysis_results = {
    'annual_pv_production_kwh': 8251.92,
    'self_supply_rate_percent': 54,
    'self_consumption_percent': 42,
}
company_info = {
    'name': 'Muster Solar GmbH',
    'street': 'Hauptstraße 1',
    'zip_code': '98765',
    'city': 'Solingen',
    'phone': '+49 555 123',
    'email': 'info@mustersolar.de',
    'website': 'https://mustersolar.de',
}

out = pg.generate_main_template_pdf_bytes(project_data, analysis_results, company_info)

out_path = Path('test_main6.pdf')
if out:
    out_path.write_bytes(out)
    print('OK bytes:', len(out))
    print('Wrote:', str(out_path.resolve()))
else:
    print('Failed: no bytes')
