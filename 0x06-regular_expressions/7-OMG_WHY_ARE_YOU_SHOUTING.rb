#!/usr/bin/env ruby
# The regular expression must be only matching: capital letters

print ARGV[0].scan(/[A-Z]/).join
