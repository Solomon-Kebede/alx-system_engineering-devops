#!/usr/bin/env ruby
pattern = /^h.n$/
argstr = ARGF.argv[0]
result = argstr.scan(pattern).flatten
for i in result
	puts i
end
if i.nil?
	puts
end
