"""White Doe, 2026: reproducible design calculation, not observed cremation data."""
import csv
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

def capacity(kg):
    pounds = Decimal(str(kg)) / Decimal('0.45359237')
    cubic_inches = pounds * Decimal('1.1') + Decimal(3)
    ml = cubic_inches * Decimal('16.387064')
    return pounds, cubic_inches, int(ml.to_integral_value(rounding=ROUND_CEILING))

if __name__ == '__main__':
    with Path(__file__).with_name('capacity-by-weight.csv').open('w', newline='', encoding='utf-8') as f:
        out = csv.writer(f)
        out.writerow(['pet_weight_kg', 'pet_weight_lb', 'calculated_capacity_cubic_inches', 'calculated_capacity_ml_rounded_up', 'source_url'])
        for half in range(1,81):
            kg = Decimal(half) / 2
            lb, ci, ml = capacity(kg)
            out.writerow([kg, format(lb,'.8f'), format(ci,'.8f'), ml, 'https://whitedoeurns.com/pages/pet-urn-size-guide'])
