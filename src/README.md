# Web Server with TLS
## Root Certificate Authority Key (Private Key)
```sh
openssl req -x509 -nodes -new -sha256 -days 356 -newkey rsa:2048 -keyout LocalCA.key -out LocalCA.pem -subj "/C=US/CN=Local-Root-CA"
```

## Self Signed Root Certificate (Public Key)
```sh
openssl x509 -outform pem -in LocalCA.pem -out LocalCA.crt
```

## LocalHost Private Key & Certificate Signing Request (CSR)
```sh
openssl req -new -nodes -newkey rsa:2048 -keyout localhost.key -out localhost.csr -subj "/C=US/ST=Texas/L=Dallas/O=Local-Host/CN=localhost.local"
```

## LocalHost Certificate (Public Key)
```sh
openssl x509 -req -sha256 -days 356 -in localhost.csr -CA LocalCA.pem -CAkey LocalCA.key -CAcreateserial -extfile domains.conf -out localhost.crt
```

## Import Root CA 
On MacOS import the LocalCA (Root CA) certificate into keychain and set the trust to "Always allow".