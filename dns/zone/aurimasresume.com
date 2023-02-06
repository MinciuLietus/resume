$TTL 86400
@       IN      SOA aurimasresume.com. *.aurimasresume.com. (
                    202      ; Serial
                    600      ; Refresh
                    3600     ; Retry
                    1209600  ; Expire
                    3600)    ; Negative Cache TTL

@       IN      NS      aurimasresume.com.
@       IN      A       127.0.0.1
www     IN      A       127.0.0.1
