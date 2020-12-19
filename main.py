import pandas as pd

def main():
    d = {'key': [1, 2, 3, 4, 5, 6, 7], 'val': ["200AAA 50LT XD",
                                   "200AAA 50LTXD",
                                   "200AAA 50LTXD",
                                   "200 AAA 50 LT XD",
                                   "200AAA50LTXD",
                                   "PQ 200 AAA 50 LT XD",
                                   "PQ 50LT 200 AAA XD"]}

    df = pd.DataFrame(data=d)   # Define a simple Pandas Dataframe to test the extraction phase
    
    # Perform extraction
    df['AAA'], df['LT'] = df['val'].str.extract(r'([\d]*) *AAA'), df['val'].str.extract(r'([\d]*) *LT')
    
    # Show results
    print(df.head())


if __name__ == '__main__':
    main()
