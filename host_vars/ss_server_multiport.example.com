---

shadowsocks_servers:

  multiport:
    port_password:
      38838: "ssserver-very-long-password-38838"
      38839: "ssserver-very-long-password-38839"
      38840: "ssserver-very-long-password-38840"
    enable_udp: true
