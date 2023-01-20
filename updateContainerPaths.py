import re 

containers = {}
with open('working_directory/nextflow.config', 'r') as f:
    for line in f:
        match = re.search(r'container = ([\'"])(.*?)\1', line)
        if match:
            old_path = match.group(2)
            # Add the container path and its new path to the dictionary
            new_path = '/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/' + '/'.join(old_path.split('/')[5:]).rstrip('.img')
            containers[old_path] = new_path

with open('working_directory/nextflow.config', 'r') as f:
    file_str = f.read()

# Replace old paths with new paths
for old_path, new_path in containers.items():
    # Use regular expressions to find and replace the container paths
    file_str = file_str.replace(old_path, new_path)

# Open the file for writing
with open('new.config', 'w') as f:
    # Write the updated file string
    f.write(file_str)