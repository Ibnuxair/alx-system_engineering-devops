#!/usr/bin/env ruby

# Get the log line as a command line argument
log_line = ARGV[0]

# Regular expression to extract sender, receiver, and flags
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Match the regular expression against the log line
match_data = log_line.match(regex)

if match_data
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  # Join the extracted values with commas
  result = [sender, receiver, flags].join(",")

  puts result
else
  puts "Invalid log line format."
end
