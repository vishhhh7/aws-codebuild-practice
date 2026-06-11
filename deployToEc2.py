import paramiko

# EC2 Details
host = "3.110.103.25"
username = "ubuntu"
key = r"C:\Users\vanga\Downloads\compute-server.pem"

# Local Python file to upload
local_file = r"E:\Projects\Vishakha Project\python\numbers_analysis.py"

# Destination on EC2
remote_file = "/home/ubuntu/numbers_analysis.py"

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to EC2
ssh.connect(
    hostname=host,
    port=22,
    username=username,
    key_filename=key
)

print("Connected to EC2 successfully!")

# Upload the file using SFTP
sftp = ssh.open_sftp()
sftp.put(local_file, remote_file)
sftp.close()

print("numbers_analysis.py uploaded successfully!")

# Execute the uploaded file
stdin, stdout, stderr = ssh.exec_command(
    f"python3 {remote_file}"
)

# Print output
print("\n===== OUTPUT =====")
print(stdout.read().decode())

# Print errors if any
error = stderr.read().decode()
if error:
    print("===== ERROR =====")
    print(error)

# Close SSH connection
ssh.close()
print("Connection closed.")
