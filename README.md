# Pandas-values-extracting-
Extracting Values from Pandas dataframe column indipendently from ordering and spacing.
NB: each numeric value must be followed by its key.

Example:

| Str               |  AAA  | LT |
|-------------------|-------|----|
| "200AAA 50LT XD"  |  200  | 50 |
| "200AAA 50LTXD"   |  200  | 50 |
| "200AAA 50LTXD"   |  200  | 50 |
| "200 AAA 50 LT XD"|  200  | 50 |
| "200AAA50LTXD"    |  200  | 50 |
| "PQ 200 AAA 50 LT XD" |  200 | 50 |
| "PQ 50LT 200 AAA XD"  |  200 | 50 |
