firewall 
# Install ufw
sudo apt update
sudo apt install ufw

# Enable ufw
sudo ufw enable

# Set default deny
sudo ufw default deny incoming

# Allow specific ports
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp

# Check status
sudo ufw status
