 # A simple DNA analysis tool
sequence = "CCGTAGCTAAGCTAG"

# Calculate counts
g_count = sequence.count('G')
c_count = sequence.count('C')

# Calculate percentage
gc_content = ((g_count + c_count) / len(sequence)) * 100

print(f"sequence: {sequence}")
print(f"The GC Content is:{gc_content:.2f}%")

