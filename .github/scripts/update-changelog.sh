#!/bin/bash

log_file="$1"
output_file="docs/updates.txt"
current_time=$(date +"%F %H:%M")
formatted_output="# $current_time"

while IFS= read -r message; do
    pr_number=$(echo "$message" | grep -oE '\(#[0-9]+\)$' | tr -d '(#)')
    formatted_message=$(echo "$message" | sed -E 's/ \(#[0-9]+\)$//')
    formatted_output+="
- [$formatted_message](https://github.com/TRaSH-Guides/Guides/pull/${pr_number})"
done < "$log_file"

formatted_output+="\n"

{
    echo -e "$formatted_output"
    cat "$output_file"
} > "${output_file}.tmp" && mv "${output_file}.tmp" "$output_file"
