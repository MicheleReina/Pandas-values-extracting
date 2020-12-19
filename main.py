import pandas as pd

def main():
    d = {'key': [1, 2, 3, 4, 5, 6, 7], 'val': ["200AAA 50LT XD",
                                   "200AAA 50LTXD",          # Extra parts at end
                                   "200AAA 50LTXD",            # Different combinations of spacing
                                   "200 AAA 50 LT XD",
                                   "200AAA50LTXD",            # No space
                                   "PQ 200 AAA 50 LT XD",     # Extra parts at begin
                                   "PQ 50LT 200 AAA XD"]}     # Inverted order

    df = pd.DataFrame(data=d)   # Define a simple Pandas Dataframe to test the extraction phase
    
    # Perform extraction
    df['AAA'], df['LT'] = df['val'].str.extract(r'([\d]*) *AAA'), df['val'].str.extract(r'([\d]*) *LT')  # Can be easily extended to N values ....
    
    # Show results
    print(df.head())


if __name__ == '__main__':
    main()
