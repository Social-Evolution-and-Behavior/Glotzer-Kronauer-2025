#!/bin/bash

# Input directory with data files 
input_dir='../KDL20220513_rRNAdepletionRNAseq/data/'

# Check if input directory exists
if [ ! -d "$input_dir" ]; then
    echo "Input directory not found."
    exit 1
fi

# Output directory 
output_dir='data_renamed/'

# Make output directory if it doesn't exist
mkdir -p "$output_dir"

# Get list of .bam files in the input directory
bam_files=($(ls "$input_dir"*.bam 2>/dev/null))

# Check if BAM files exist
if [ ${#bam_files[@]} -eq 0 ]; then
    echo "No BAM files found in $input_dir."
    exit 1
fi

# Activate conda environment with samtools
eval "$(conda shell.bash hook)"
conda activate samtools-env

# Ensure samtools is installed
if ! command -v samtools &> /dev/null; then
    echo "samtools could not be found. Please install samtools."
    exit 1
fi

# Iterate through bam files and extract strand coverage
for bam_file in "${bam_files[@]}"; do
    if [ -f "$bam_file" ]; then
        echo "Processing BAM File: $bam_file"
        
        # Extract header, modify chromosome names, and save to a temporary header file
        base_name=$(basename "$bam_file" .bam)
        header_path="${output_dir}${base_name}_header.sam"
        samtools view -H "$bam_file" | \
        sed -e 's/NC_039506.1/Chr1/' \
            -e 's/NC_039507.1/Chr2/' \
            -e 's/NC_039508.1/Chr3/' \
            -e 's/NC_039509.1/Chr4/' \
            -e 's/NC_039510.1/Chr5/' \
            -e 's/NC_039511.1/Chr6/' \
            -e 's/NC_039512.1/Chr7/' \
            -e 's/NC_039513.1/Chr8/' \
            -e 's/NC_039514.1/Chr9/' \
            -e 's/NC_039515.1/Chr10/' \
            -e 's/NC_039516.1/Chr11/' \
            -e 's/NC_039517.1/Chr12/' \
            -e 's/NC_039518.1/Chr13/' \
            -e 's/NC_039519.1/Chr14/' > "$header_path"

        if [ $? -ne 0 ]; then
            echo "Failed to create header for $bam_file"
            rm -f "$header_path"
            continue
        fi

        # Replace the header in the BAM file with the modified header and create a new BAM file
        output_path="${output_dir}${base_name}_renamed.bam"
        samtools reheader "$header_path" "$bam_file" > "$output_path"

        if [ $? -ne 0 ]; then
            echo "Failed to reheader $bam_file"
            rm -f "$header_path" "$output_path"
            continue
        fi

        # Clean up temporary header file
        rm "$header_path"
        echo "Chromosome names updated and saved to $output_path"
    else
        echo "File not found: $bam_file"
    fi
done

# Final confirmation message
echo "Chromosome names updated for all BAM files in $output_dir"
