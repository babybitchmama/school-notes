#!/bin/bash

# Define input and output file
input_pdf="master.pdf"
output_pdf="extracted_pages.pdf"

# Define the page ranges
page_ranges="183-189 194-195 227-231 233-235 237-241 243-245 258-261"

# Extract the specified pages using pdftk
pdftk "$input_pdf" cat $page_ranges output "$output_pdf"

echo "Extracted pages saved to $output_pdf"
