import numpy as np 

class Transcriptome:
    def __init__(self):
        self.genes = {}
        self.transcripts_to_genes = {}

    def add_gene(self, gene):
        """Add gene to the transcriptome"""
        self.genes[gene.name] = gene

    def get_gene(self, name):
        """Get gene by name"""
        return self.genes.get(name, None)
    
    def remove_gene(self, name):
        """Remove gene by name"""
        if name in self.genes:
            del self.genes[name]

    def search_genes(self, query):
        """Search for genes by name"""
        results = []
        for gene in self.genes.values():
            if query.lower() in gene.name.lower():
                results.append(gene)
        return f"Found {len(results)} genes matching query '{query}': {results}"
    
    def search_genes_by_location(self, chromosome, coordinate): 
        """Search for genes by location (chromosome and single coordinate)"""
        result = [] 
        for gene in self.genes.values():
            if gene.chromosome == chromosome and len(gene.transcripts)>0: 
                bounds = gene.get_transcript_longest_bounds().get_bounds()
                if bounds[0] <= coordinate <= bounds[1]:
                    result.append(gene)
        return result
    
    def get_transcript(self, transcript_id): 
        """Get transcript object from transcript ID"""
        gene_name = self.get_gene_from_transcript(transcript_id)
        if gene_name is not None:
            gene_object = self.get_gene(gene_name)
            for transcript in gene_object.transcripts:
                if transcript_id in transcript.name:
                    return transcript
        return None

    def get_gene_from_transcript(self, transcript_id):
        """Get gene name from transcript ID (useful for parsing blast results)"""
        # Make a dictionary for faster lookup
        if len(self.transcripts_to_genes) == 0:
            transcripts_to_genes = {}
            for gene in self.genes.values():
                for transcript in gene.transcripts:
                    transcripts_to_genes[transcript.name] = gene.name
            self.transcripts_to_genes = transcripts_to_genes
        
        # First try to get an exact match
        gene_name = self.transcripts_to_genes.get(transcript_id)
        if gene_name is not None:
            return gene_name
        
        # If no exact match, search for partial matches
        partial_matches = [gene for transcript, gene in self.transcripts_to_genes.items() if transcript_id in transcript]
        if len(partial_matches) == 1:
            return partial_matches[0]
        elif len(partial_matches) > 1:
            print(f"Warning: Multiple partial matches found for {transcript_id}. Returning the first match.")
            return partial_matches[0]
        
        # Return None if no match is found
        return None

    def __str__(self):
        return f"Transcriptome(genes={len(self.genes)})"
    
    def __repr__(self):
        return self.__str__()

    
class Gene:
    def __init__(self, id, name):
        self.id = id
        self.name = name 
        self.transcripts = []
        self.chromosome = ""
        self.strand = ""
    
    def add_transcript(self, transcript):
        """Add transcript to the gene"""
        self.transcripts.append(transcript)

    def get_transcript_longest_cds(self):
        """Get the transcript with the longest CDS"""
        if len(self.transcripts) == 0: 
            raise ValueError("No transcripts found for this gene")
        else: 
            return self.transcripts[np.argmax([transcript.cds_length for transcript in self.transcripts])]
        
    def get_transcript_longest_bounds(self): 
        """Get the transcript with the longest bounds"""
        if len(self.transcripts) == 0: 
            raise ValueError("No transcripts found for this gene")
        else:
            bounds = [transcript.get_bounds() for transcript in self.transcripts]
            bound_lengths = [abs(x[1] - x[0]) for x in bounds]
            return self.transcripts[np.argmax(bound_lengths)] 

    def __str__(self):
        return f"Gene(name={self.name}, id={self.id}, transcripts={len(self.transcripts)}, chromosome={self.chromosome}, strand={self.strand})"
    
    def __repr__(self):
        return self.__str__()

class Transcript:
    def __init__(self, name):
        self.name = name
        self.cds_sequence = "" 
        self.cds_length = 0 
        self.mrna_sequence = "" 
        self.dna_sequence = "" 
        self.chromosome = ""
        self.strand = ""
        self.position = None
        self.biotype = "" 
        self.utrs = []
        self.exons = []
        self.cds = [] 
        self.introns = []

    def get_bounds(self): 
        """Get the start and end position of the transcript"""
        combined = self.utrs[:] + self.exons[:] + self.introns[:] + self.cds[:]
        possible_bounds = [x.position for x in combined if x is not None]
        possible_bounds = [item for sublist in possible_bounds for item in sublist]
        if len(possible_bounds) < 2: 
            return None
        else:
            return [np.min(possible_bounds),np.max(possible_bounds)]
    
    def __str__(self):
        return (f"Transcript(name={self.name}, {self.cds_length}bp CDS, {self.chromosome}:{self.position[0]}-{self.position[1]}, exons={len(self.exons)}, introns={len(self.introns)}, utrs={len(self.utrs)})")
    
    def __repr__(self):
        return self.__str__()


class Exon:
    def __init__(self, transcript, sequence, chromosome, position, strand):
        self.transcript = transcript
        self.sequence = sequence
        self.chromosome = chromosome
        self.position = position
        self.strand = strand
    
    def __str__(self):
        return f"Exon(transcript={self.transcript}, {self.chromosome}:{self.position[0]}-{self.position[1]}, strand={self.strand})"
    
    def __repr__(self):
        return self.__str__()
    
class CDS: 
    def __init__(self, transcript, sequence, chromosome, position, strand):
        self.transcript = transcript
        self.sequence = sequence
        self.chromosome = chromosome
        self.position = position
        self.strand = strand
    
    def __str__(self):
        return f"CDS(transcript={self.transcript}, {self.chromosome}:{self.position[0]}-{self.position[1]}, strand={self.strand})"
    
    def __repr__(self):
        return self.__str__()
    

class Intron:
    def __init__(self, transcript, sequence, chromosome, position, strand):
        self.transcript = transcript
        self.sequence = sequence
        self.chromosome = chromosome
        self.position = position
        self.strand = strand

    def __str__(self):
        return f"Intron(transcript={self.transcript}, {self.chromosome}:{self.position[0]}-{self.position[1]}, strand={self.strand})"
    
    def __repr__(self):
        return self.__str__()

class UTR:
    def __init__(self, transcript, sequence, chromosome, position, strand, utr_type):
        self.transcript = transcript
        self.sequence = sequence
        self.chromosome = chromosome
        self.position = position
        self.strand = strand
        self.utr_type = utr_type

    def __str__(self):
        return f"UTR(transcript={self.transcript}, type={self.utr_type}, {self.chromosome}:{self.position[0]}-{self.position[1]}, strand={self.strand})"
    
    def __repr__(self):
        return self.__str__()

