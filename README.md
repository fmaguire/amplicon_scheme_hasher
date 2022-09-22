# Amplicon Scheme Hasher

Very basic stdlib only python tool for hashing (sha256) the fixed parts (i.e., reference, start, stop, and strand) of an amplicon scheme bed file. 

This tool can be run in two modes `--bed` which will provide a hash for a single input bed file:

    >>> python amplicon_scheme_hasher.py --bed data/artic_v3.bed
    data/artic_v3.bed hash: 58329945ae4978b849045a753a80d9ea7573f54e65f55f04356b556dacb06c4c

Alternatively you can use this with `--compare` to hash and compare 2 or more bed files: 

    >>> python amplicon_scheme_hasher.py --compare data/artic_v3.bed data/artic_v3_alt.bed data/freed_v1.bed 
    data/artic_v3_alt.bed hash: 58329945ae4978b849045a753a80d9ea7573f54e65f55f04356b556dacb06c4c
    data/artic_v3.bed hash: 58329945ae4978b849045a753a80d9ea7573f54e65f55f04356b556dacb06c4c
    data/freed_v1.bed hash: 48045151bd9acb30cf3efc9d6944e751112e93d49de0d155002e67d456a5a14f
    
    data/artic_v3_alt.bed and data/artic_v3.bed MATCH
    data/artic_v3_alt.bed and data/freed_v1.bed DO NOT MATCH
    data/artic_v3.bed and data/freed_v1.bed DO NOT MATCH

As you can see despite a different amplicon naming scheme in `data/artic_v3.bed` and `data/artic_v3_alt.bed` these hash to the same values as the hashing is only based on reference name, start, stop, and strand.
This is also robust to differences in primer orders in the bed file i.e., the same file sorted differently will still hash to the same value.
