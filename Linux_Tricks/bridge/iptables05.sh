iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -A FORWARD -i br0 -o eth3 -j ACCEPT
iptables -A FORWARD -i eth3 -o br0 -m state --state ESTABLISHED,RELATED -j ACCEPT 
iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o eth3 -j MASQUERADE
