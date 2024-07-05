#!/bin/bash

log="$1"
base_url="https://github.com/TRaSH-Guides/Guides/pull/"
output_file="docs/updates.txt"
current_time=$(date +"%F %H:%M")
formatted_output="# $current_time"

while IFS= read -r message; do
    pr_number=$(echo "$message" | grep -oE '#[0-9]+' | tr -d '#')
    formatted_message=$(echo "$message" | sed -E 's/ \(#.*//')
    formatted_output+="
- [$formatted_message](${base_url}${pr_number})"
done <<< "$log"

formatted_output+="\n"

{
    echo -e "$formatted_output"
    cat "$output_file"
} > "${output_file}.tmp" && mv "${output_file}.tmp" "$output_file"

# Inform the user
echo "Output prepended to $output_file"
