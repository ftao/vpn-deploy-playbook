function FindProxyForURL(url, host) {
    if (isPlainHostName(host) || (host == "127.0.0.1") || (host == "localhost")
    {% for subnet,mask in intranet_addresses %}
    || (isInNet(host, "{{ subnet }}", "{{ mask }}"))
    {% endfor %}
    {% for domain in direct_domains %}
    || dnsDomainIs(host, "{{ domain }}")
    {% endfor %} ){
        return  "DIRECT";
    }
    {% if proxy_server_type == "spdy" %}
    return  "HTTPS {{ proxy_server_host }}:{{ proxy_server_port }};";
    {% elif proxy_server_type == "socks5" %}
    return  "SOCKS5 {{ proxy_server_host }}:{{ proxy_server_port }}; SOCKS {{ proxy_server_host }}:{{ proxy_server_port }};";
    {% endif %}
    {% if proxy_server_type == "http" %}
    return  "PROXY {{ proxy_server_host }}:{{ proxy_server_port }};";
    {% endif %}
}
