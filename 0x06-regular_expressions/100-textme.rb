#!/usr/bin/env ruby
pattern = /from:(.*)\W{3}to:(.*)\W{3}flags:(.*)\W{3}msg/
argstr = ARGF.argv[0].inspect
result = argstr.scan(pattern).flatten
for i in result
	print i
	print ","
end
if not i.nil?
	puts
end
