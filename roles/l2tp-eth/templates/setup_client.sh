#!/bin/sh
CLIENT_PORT="{{ l2tp_eth_client_port }}"
CLIENT_IP="{{ l2tp_eth_client_ip }}"
SERVER_IP="{{ l2tp_eth_client_remote_ip }}"
SERVER_PORT="{{ l2tp_eth_client_remote_port }}"
LOCAL_IP="{{ l2tp_eth_client_local_ip }}"
PEER_IP="{{ l2tp_eth_client_peer_ip }}"
ETH_NAME="{{ l2tp_eth_name }}"
MTU="{{ l2tp_eth_mtu }}"
SESSION="0x{{ l2tp_eth_session }}"
COOKIE="{{ l2tp_eth_cookie }}"

modprobe l2tp_eth
ip l2tp del tunnel tunnel_id 1 || true
ip l2tp add tunnel local $CLIENT_IP remote $SERVER_IP tunnel_id 1 peer_tunnel_id 1 encap udp udp_sport $CLIENT_PORT udp_dport $SERVER_PORT
ip l2tp add session tunnel_id 1 session_id $SESSION peer_session_id $SESSION cookie $COOKIE peer_cookie $COOKIE
ip addr add $LOCAL_IP peer $PEER_IP dev $ETH_NAME
ip link set $ETH_NAME up mtu $MTU

{% if l2tp_eth_client_default_gateway %}
{% if l2tp_eth_client_origin_gw %}
ORIGIN_GW="{{ l2tp_eth_client_origin_gw  }}"
{% else %}
ORIGIN_GW=`ip route show 0.0.0.0/0 dev {{ l2tp_eth_client_if }} | cut -d\  -f3`
{% endif %}
ip route add $SERVER_IP via $ORIGIN_GW dev {{ l2tp_eth_client_if }} || true
ip route add 0.0.0.0/1 via $PEER_IP dev  $ETH_NAME || true
ip route add 128.0.0.0/1 via $PEER_IP dev $ETH_NAME || true
{% endif %}
