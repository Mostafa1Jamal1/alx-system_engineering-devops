#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/\[from:(.*?)\]/)
RECEIVER = ARGV[0].scan(/\[to:(\+?\d+)\]/)
FLAGS = ARGV[0].scan(/\[flags:(.*?)\]/)
puts "#{SENDER.join(',')},#{RECEIVER.join(',')},#{FLAGS.join(',')}"
