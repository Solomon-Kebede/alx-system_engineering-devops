#!/usr/bin/env ruby
pattern = /from:(.*)\W{3}to:(.*)\W{3}flags:(.*)\W{3}msg/
argstr = ARGF.argv[0].inspect
result = argstr.scan(pattern).flatten
len = result.length
puts len
for i in result
	print i
	if (result.find_index(i)) != (len - 1)
		print ","
	end
end
puts
puts
if not i.nil?
	puts
end
