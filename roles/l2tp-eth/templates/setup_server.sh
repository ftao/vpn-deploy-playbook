#!/bin/sh
SNAT_IP="{{ l2tp_eth_server_snat_ip }}"
SNAT_PORT="{{ l2tp_eth_client_port }}"
SERVER_PORT="{{ l2tp_eth_server_port }}"
SERVER_IF="{{ l2tp_eth_server_if }}"
SERVER_IP="{{ l2tp_eth_server_ip }}"
LOCAL_IP="{{ l2tp_eth_server_local_ip }}"
PEER_IP="{{ l2tp_eth_server_peer_ip }}"
ETH_NAME="{{ l2tp_eth_name }}"
MTU="{{ l2tp_eth_mtu }}"
SESSION="0x{{ l2tp_eth_session }}"
COOKIE_HIGH="0x{{ l2tp_eth_cookie[:8] }}"
COOKIE_LOW="0x{{ l2tp_eth_cookie[8:] }}"
COOKIE="{{ l2tp_eth_cookie }}"

modprobe l2tp_eth

#clean up 
iptables -t nat -D INPUT -i $SERVER_IF -p udp --dport $SERVER_PORT -m u32 --u32 "0>>22&0x3C@12 = $SESSION && 0>>22&0x3C@16 = $COOKIE_HIGH && 0>>22&0x3C@20 = $COOKIE_LOW" -j SNAT --to-source $SNAT_IP:$SNAT_PORT 2>/dev/null
ip l2tp del tunnel tunnel_id 1 || true

#setup
iptables -t nat -A INPUT -i $SERVER_IF -p udp --dport $SERVER_PORT -m u32 --u32 "0>>22&0x3C@12 = $SESSION && 0>>22&0x3C@16 = $COOKIE_HIGH && 0>>22&0x3C@20 = $COOKIE_LOW" -j SNAT --to-source $SNAT_IP:$SNAT_PORT
ip l2tp add tunnel local $SERVER_IP remote $SNAT_IP tunnel_id 1 peer_tunnel_id 1 encap udp udp_sport $SERVER_PORT udp_dport $SNAT_PORT
ip l2tp add session tunnel_id 1 session_id $SESSION peer_session_id $SESSION cookie $COOKIE peer_cookie $COOKIE
ip addr add $LOCAL_IP peer $PEER_IP dev $ETH_NAME
ip link set $ETH_NAME up mtu $MTU
