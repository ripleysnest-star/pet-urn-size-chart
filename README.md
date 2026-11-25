# Pet urn size chart and reproducible capacity calculator

Creator: White Doe. Version 1.0.0, 13 November 2026.

Source and interactive guide: [White Doe pet urn size guide](https://whitedoeurns.com/pages/pet-urn-size-guide)

Citable archived copy: Zenodo, DOI [10.5281/zenodo.24207132](https://doi.org/10.5281/zenodo.24207132). This repository mirrors that record so it can be forked, diffed and used straight from GitHub.

Free to put on your own site: an [embeddable pet urn size calculator](https://whitedoeurns.com/pages/pet-urn-size-guide#use-on-your-site) (kg and lb, no tracking).

This small reference dataset makes White Doe's published pet urn sizing method reusable in a spreadsheet or calculator. It is a design calculation, not measured cremation data, a scientific study, or an independent industry standard. It contains no customer, sales, keyword or search data.

## Files

- `white-doe-size-chart.csv`: the three published size bands and their nominal capacities.
- `capacity-by-weight.csv`: calculated internal capacity for weights from 0.5 to 40 kg in 0.5 kg increments. These are calculation outputs, not observations.
- `calculate.py`: a dependency-free generator for the calculated table.

## Method and units

Required internal space in cubic inches = (weight in pounds * 1.10) + 3.
This means one cubic inch for each pound the pet weighed, plus a tenth, plus 3 cubic inches. Convert kilograms using 1 pound = 0.45359237 kg. Convert cubic inches using 1 cubic inch = 16.387064 ml. The generated millilitre value is rounded upwards to the next whole ml; unrounded intermediate cubic-inch values are also included.

The source guide's catalogue capacities are rounded nominal figures: Small, up to 15 kg, 645 ml; Medium, up to 30 kg, 1,240 ml; Large, up to 40 kg, 1,640 ml. Small differences between these nominal figures and exact calculated outputs reflect rounding; keep the two columns/files distinct. For a particular container or an existing bag of ashes, check the actual internal space and opening rather than substituting an exterior measurement.

## Reuse and citation

Please credit: White Doe (2026), *Pet urn size chart and reproducible capacity calculator*, version 1.0.0, and link to the source guide: https://whitedoeurns.com/pages/pet-urn-size-guide

Released under Creative Commons Attribution 4.0 International. Brand names and logos are not included in the data licence. Contact: hello@whitedoeurns.com.
