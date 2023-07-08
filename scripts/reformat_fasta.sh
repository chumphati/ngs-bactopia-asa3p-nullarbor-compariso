#!/bin/bash

input_file="protein.faa"
output_file="protein_reformat.faa"

while IFS= read -r line
do
  if [[ $line == ">"* ]]; then
    id=$(echo "$line" | cut -d' ' -f1)
    info=$(echo "$line" | cut -d' ' -f2-)
    cpt=$(echo "$info" | grep -o "~~~" | wc -l)

    if [[ $cpt -eq 1 ]]; then
      new_info="unknown~~~${info/ / }"
    else
      new_info="$info"
    fi

    new_line="${id} ${new_info}"
    echo "$new_line" >> "$output_file"
  else
    echo "$line" >> "$output_file"
  fi
done < "$input_file"
