#!/bin/bash

# Input directory with data files 
input_dir='data_renamed/'

# Check if input directory exists
if [ ! -d "$input_dir" ]; then
    echo "Input directory not found."
    exit 1
fi

# Output directory 
output_dir='first_of_pair_strand_coverage/'

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

# Function to process each BAM file
process_bam_file() {
    local bam_file="$1"
    local output_dir="$2"
    
    base_name=$(basename "$bam_file" .bam)

    # Forward strand coverage
    output_path_bam_fwd="${output_dir}${base_name}_forward_strand_pairs.bam"
    output_path_coverage_fwd="${output_dir}${base_name}_forward_strand_coverage.txt"
    samtools view -h "$bam_file" | \
        awk '($2 == 83 || $2 == 163) || $1 ~ /^@/' | \
        samtools view -b - > "$output_path_bam_fwd"
    samtools depth -aa -Q 20 "$output_path_bam_fwd" > "$output_path_coverage_fwd"
    echo "Forward strand coverage file created: $output_path_coverage_fwd"
    rm "$output_path_bam_fwd" # Remove temporary BAM file

    # Reverse strand coverage
    output_path_bam_rev="${output_dir}${base_name}_reverse_strand_pairs.bam"
    output_path_coverage_rev="${output_dir}${base_name}_reverse_strand_coverage.txt"
    samtools view -h "$bam_file" | \
        awk '($2 == 99 || $2 == 147) || $1 ~ /^@/' | \
        samtools view -b - > "$output_path_bam_rev"
    samtools depth -aa -Q 20 "$output_path_bam_rev" > "$output_path_coverage_rev"
    echo "Reverse strand coverage file created: $output_path_coverage_rev"
    rm "$output_path_bam_rev" # Remove temporary BAM file
}

export -f process_bam_file

# Process each BAM file in parallel
for bam_file in "${bam_files[@]}"; do
    process_bam_file "$bam_file" "$output_dir" &
done

# Wait for all background processes to complete
wait

# Final confirmation message
echo "Forward and reverse strand coverage files based on first-of-pair orientation created in $output_dir"


