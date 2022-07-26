#!/usr/bin/env ruby
pattern = /School/
argstr = ARGF.argv[0].inspect
results = argstr.scan(pattern).flatten
for i in results
	print i
end
if not i.nil?
	puts
end
