def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings("hello", "world"))
print(concat_strings("raymond", "francois", "saade", sep="_"))
