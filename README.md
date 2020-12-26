# Pandas-values-extracting-
Extracting Values from Pandas dataframe column indipendently from ordering and spacing.
NB: each numeric value must be followed by its key.

Example:

| Str               |  AAA  | LT | Descr. | 
|-------------------|-------|----|--------|
| "200AAA 50LT XD"  |  200  | 50 |Extra parts at end |
| "200AAA 50LTXD"   |  200  | 50 | Different combinations of spacing |
| "200AAA 50LTXD"   |  200  | 50 |
| "200 AAA 50 LT XD"|  200  | 50 | All spaced |
| "200AAA50LTXD"    |  200  | 50 | No space|
| "PQ 200 AAA 50 LT XD" |  200 | 50 | Extra parts at begin |
| "PQ 50LT 200 AAA XD"  |  200 | 50 | Inverted order |
