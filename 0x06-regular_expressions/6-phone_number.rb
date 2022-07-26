#!/usr/bin/env ruby
pattern = /\d{10}/
argstr = ARGF.argv[0].inspect
result = argstr.scan(pattern).flatten
for i in result
	result2 = argstr.split(pattern)
	if result2.join("").length == 2
		print i
	end
end
puts
