#!/usr/bin/env ruby
pattern = /[A-Z]/
argstr = ARGF.argv[0].inspect
result = argstr.scan(pattern).flatten
for i in result
	print i
end
puts
