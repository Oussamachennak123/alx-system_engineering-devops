#!/usr/bin/env ruby
#  the project instructions, create a Ruby script that accepts one argument
#  and pass it to a regular expression matching method
print ARGV[0].scan(/hbt{2,5}n/).join
