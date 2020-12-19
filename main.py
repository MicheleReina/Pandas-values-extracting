import pandas as pd

def main():
    d = {'key': [1, 2, 3, 4, 5, 6, 7], 'val': ["200AAA 50LT XD",
                                   "200AAA 50LTXD",
                                   "200AAA 50LTXD",
                                   "200 AAA 50 LT XD",
                                   "200AAA50LTXD",
                                   "PQ 200 AAA 50 LT XD",
                                   "PQ 50LT 200 AAA XD"]}

    df = pd.DataFrame(data=d)
    df['AAA'], df['LT'] = df['val'].str.extract(r'([\d]*) *AAA'), df['val'].str.extract(r'([\d]*) *LT')
    print(df.head(25))


if __name__ == '__main__':
    main()
