#!/usr/bin/env ruby
pattern = /hbt{0,}n/
argstr = ARGF.argv[0].inspect
result = argstr.scan(pattern).flatten
for i in result
	print i
end
if not i.nil?
	puts
end
