
# Drop UDP traffic for testing GAP recovery
iptables -I INPUT -p udp -d 239.255.52.123 --dport 35912  -j DROP
