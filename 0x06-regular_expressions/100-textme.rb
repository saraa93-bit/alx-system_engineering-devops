#!/usr/bin/env ruby

# Get the log file path from command line argument

log_file = ARGV[0]

# Read the log file and iterate over each line
File.readlines(log_file).each do |line|
  # Extract sender, receiver, and flags using regex
  match_data = line.match(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/)

  # If match is found
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    
    # Output the parsed data in the specified format
    puts "#{sender},#{receiver},#{flags}"
  end
end
