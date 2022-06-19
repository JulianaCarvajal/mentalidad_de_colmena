d_path = 'required_data.txt'
d_r_path = 'required_data_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    required_data = reader.readlines()
    writer.writelines(reversed(required_data))