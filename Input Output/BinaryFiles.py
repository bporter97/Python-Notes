# Same basic principles apply for writing, reading and appending binary files as they do for just regular files.
# To write to a binary file, all you have to do is put a b in front of the mode (w) as seen below.

# with open("binary", 'bw') as bin_file:
    # for i in range(17):
        # bin_file.write(bytes([i])) # binary files need to use the ".write" method in order to write to a file.
        # the "bytes" method is the data type we are returning.

# with open("binary", 'br') as binFile:
    # for b in binFile:
        # print(b)

a = 65534
b = 65535
c = 65536
d = 2998302

with open("binary2", 'bw') as bin2_file:
    bin2_file.write(a.to_bytes(2, 'big')) # 'big' stores the most significant byte first
    bin2_file.write(b.to_bytes(2, 'big'))
    bin2_file.write(c.to_bytes(4, 'big'))
    bin2_file.write(d.to_bytes(4, 'big'))
    bin2_file.write(d.to_bytes(4, 'little')) # 'little' stores the least significant byte first

with open("binary2",  'br') as bin2_file:
    e = int.from_bytes(bin2_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin2_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin2_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin2_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin2_file.read(2), 'big')
    print(i)

