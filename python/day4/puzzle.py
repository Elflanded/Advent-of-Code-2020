import pandas as pd

with open('input.py', 'r') as f:
    passports = f.read()

df = pd.DataFrame([
    {k: v for k, v in (user_data.split(":") for user_data in passport.split())} 
    for passport in passports.split("\n\n")
])


df.dropna(subset=['byr', 'pid', 'eyr', 'hgt', 'iyr', 'ecl', 'hcl'], inplace=True)

print(f'there are {len(df)} potentially valid passports (PART1)')


is_valid_colour = lambda x: all(i in '0123456789abcdef' for i in x)
df.query("""
    byr.str.len() == 4 and \
    iyr.str.len() == 4 and \
    eyr.str.len() == 4 and \
    pid.str.len() == 9 and \
    ecl.isin(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and \
    hcl.str[0] == '#' and \
    hcl.str.slice(1).apply(@is_valid_colour)
    """, engine='python', inplace=True
)

df['hgt_units'] = df.hgt.str.slice(-2)
df['hgt'] = df.hgt.str.slice(0, -2)

num_cols = ['iyr', 'eyr', 'byr', 'pid', 'hgt']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')
df.query("""
    1920 <= byr <= 2002 and \
    2010 <= iyr <= 2020 and \
    2020 <= eyr <= 2030 and \
    ((hgt_units == 'cm' and 150 <= hgt <= 193) or \
    (hgt_units == 'in' and 59 <= hgt <= 79)) and \
    ~pid.isna()
    """, engine='python', inplace=True
)

print(f'there are {len(df)} valid passports that comply with regulations (PART2)')
