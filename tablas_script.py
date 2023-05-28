def generate_table_row(year1, year2):
    row = f"""
    \\textbf{{{year1}}} & \\includegraphics[width=0.2\\textwidth]{{img_sat/NDVI_{year1}.png}} & \\includegraphics[width=0.2\\textwidth]{{img_sat/NSI_{year1}.png}} &
    \\textbf{{{year2}}} & \\includegraphics[width=0.2\\textwidth]{{img_sat/NDVI_{year2}.png}} & \\includegraphics[width=0.2\\textwidth]{{img_sat/NSI_{year2}.png}} \\\\
    \\hline
    """
    return row


start_year = 1985
end_year = 2021

rows = []

for year in range(start_year, end_year + 1, 2):
    if year == 2012:
        continue
    if year + 1 <= end_year and year + 1 != 2012:
        row = generate_table_row(year, year + 1)
    elif year != end_year and year != 2012:
        row = generate_table_row(year, "")
    rows.append(row)

table_body = "\n".join(rows)

print(table_body)

