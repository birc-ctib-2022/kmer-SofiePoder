"""Computing kmers of a string."""

kmer_list = []
def kmer(x: str, k: int) -> list[str]:
    for i in range(0,len(x)-(k-1),1):
        kmers = x[i:i+k]
        kmer_list.append(kmers)
    return kmer_list
    
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agtagtcg', 4)
    ['agta', 'gtag', 'tagt', 'agtc', 'gtcg']
    """
    ...

k_list = []
def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']
    """
    for i in range(len(x)-(k-1)):
        kmers = x[i:i+k]
        if kmers not in k_list:
            k_list.append(kmers)
    return k_list

    ...

dic_kmer = {}
def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('agtagtcg', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}
    """
    for i in range(len(x)-(k-1)):
        kmers = x[i:i+k]
        if kmers not in dic_kmer:
            dic_kmer[kmers] = 1
        else:
            dic_kmer[kmers] += 1
            
    return dic_kmer

...
