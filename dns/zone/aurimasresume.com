$TTL 86400
@       IN      SOA aurimasresume.com. *.aurimasresume.com. (
                    202      ; Serial
                    600      ; Refresh
                    3600     ; Retry
                    1209600  ; Expire
                    3600)    ; Negative Cache TTL

@       IN      NS      aurimasresume.com.
@       IN      A       ns-203.awsdns-25.com
www     IN      A       ns-833.awsdns-40.net
www     IN      A       ns-1512.awsdns-61.org
www     IN      A       ns-1995.awsdns-57.co.uk
