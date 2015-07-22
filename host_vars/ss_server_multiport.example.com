---

shadowsocks_servers:

  multiport_mannual:
    port_password:
      8838: "ssserver-very-long-password"
      8839: "ssserver-very-long-password"
    enable_udp: true


  multiport_auto:
    enable_udp: true
