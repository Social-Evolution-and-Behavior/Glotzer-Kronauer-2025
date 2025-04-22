import numpy as np 

# Function to get the reverse complement of a sequence 
def reverse_complement(sequence):
    complement = ''
    for base in sequence:
        if base == 'A':
            complement = 'T' + complement
        elif base == 'T':
            complement = 'A' + complement
        elif base == 'C':
            complement = 'G' + complement
        elif base == 'G':
            complement = 'C' + complement
        elif base == '-':
            complement = '-' + complement
    return complement


# Function to get amplifier sequences 
def get_amplifier(ampl):
    if ampl == "B1":
        upspc= "aa"
        dnspc= "ta"
        up = "GAGGAGGGCAGCAAACGG"
        dn = "GAAGAGTCTTCCTTTACG"
    elif ampl == "B2":
        upspc= "aa"
        dnspc= "aa"
        up = "CCTCGTAAATCCTCATCA"
        dn = "ATCATCCAGTAAACCGCC"
    elif ampl == "B3":
        upspc= "tt"
        dnspc= "tt"
        up = "GTCCCTGCCTCTATATCT"
        dn = "CCACTCAACTTTAACCCG"
    elif ampl == "B4":
        upspc= "aa"
        dnspc= "at"
        up = "CCTCAACCTACCTCCAAC"
        dn = "TCTCACCATATTCGCTTC"
    elif ampl == "B5":
        upspc= "aa"
        dnspc= "aa"
        up = "CTCACTCCCAATCTCTAT"
        dn = "CTACCCTACAAATCCAAT"
    else:
        print("Please try again")
    return([upspc,dnspc,up,dn])



def design_hcr_probes(sequence, amplifier): 
    # Get the reverse complement of the sequence
    sequence = reverse_complement(sequence)
    
    # Get spacers and amplifier sequences 
    uspc, dspc, upinit, dninit = get_amplifier(amplifier)
    
    # Create a list to store the probe pairs
    probe_pairs = []

    # Create a list of regions of mRNA where the probes are binding 
    probe_regions = []

    # Create a list of start and end positions for the probes
    probe_positions = []
    
    # We design 3' to 5' so we start at the end of the sequence
    position=len(sequence) 
    
    # 52 is the cutoff for fitting an entire pair at the end of the gene
    while position>=52: 
        upstream=str(sequence[position-25:position])
        downstream=str(sequence[position-52:position-27])
        percent_GC_dn = (downstream.count("G") + downstream.count("C")) / 25
        percent_GC_up = (upstream.count("G") + upstream.count("C")) / 25
        if '-' in upstream or '-' in downstream:
            position-=1
        elif percent_GC_dn > 0.75 or percent_GC_up > 0.75: # too high GC content 
            position-=1
        elif percent_GC_dn < 0.25 or percent_GC_up < 0.25: # too low GC content
            position-=1
        elif "GGGGG" in downstream or "GGGGG" in upstream:
            position-=5
        elif "CCCCC" in downstream or "CCCCC" in upstream:
            position-=5
        elif "AAAAA" in downstream or "AAAAA" in upstream:
            position-=5
        elif "TTTTT" in downstream or "TTTTT" in upstream:
            position-=5
        else:
            primer_up = upinit+uspc+upstream 
            primer_dn = downstream+dspc+dninit
            probe_pairs.append([primer_up, primer_dn])
            probe_regions.append(reverse_complement(sequence[position-52:position]))
            probe_positions.append([len(sequence) - position, len(sequence) - position + 52])
            position-=54    
            
    return probe_pairs, probe_regions, probe_positions


def reverse_string(string): 
    return ''.join([string[i] for i in np.linspace(len(string)-1, 0, len(string)).astype('int')])


def overlapping(chr1, start1, end1, chr2, start2, end2):
    """Returns True if the two intervals overlap by at least one base pair, False otherwise."""
    if chr1 != chr2:
        return False
    if start1 < start2 < end1:
        return True
    if start1 < end2 < end1:
        return True
    if start2 < start1 < end2:
        return True
    if start2 < end1 < end2:
        return True
    return False