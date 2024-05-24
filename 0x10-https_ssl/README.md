# 0x10. HTTPS SSL

## Overview

**HTTPS** (HyperText Transfer Protocol Secure) and **SSL** (Secure Sockets Layer) are fundamental technologies for securing communications over the internet. HTTPS is the secure version of HTTP, the protocol over which data is sent between your browser and the website you are connected to. SSL is the standard security technology for establishing an encrypted link between a web server and a browser.

## HTTPS

### What is HTTPS?

HTTPS is an extension of HTTP and is used for secure communication over a computer network. It ensures that data sent between the user and the website is encrypted, making it harder for attackers to intercept and read.

### How HTTPS Works

1. **Client Request**: The user connects to a website using HTTPS.
2. **Server Response**: The server sends its SSL certificate to the client's browser.
3. **SSL Handshake**: The client's browser and the web server engage in an SSL handshake, establishing a secure connection.
4. **Secure Connection**: Data transferred between the client and the server is encrypted, ensuring privacy and data integrity.

### Benefits of HTTPS

- **Encryption**: Encrypts the data exchanged between the user and the server, protecting it from eavesdroppers.
- **Data Integrity**: Ensures that data is not modified during transfer.
- **Authentication**: Verifies that the user is communicating with the intended website.

## SSL

### What is SSL?

SSL is a standard security protocol for establishing encrypted links between a web server and a browser in an online communication. It ensures that all data passed between the web server and browsers remain private and integral.

### How SSL Works

1. **SSL Certificate**: The web server presents an SSL certificate to the client.
2. **Public and Private Keys**: SSL uses a pair of keys, a public key and a private key, to establish a secure connection.
3. **Encryption**: Data transferred over the connection is encrypted using symmetric encryption after the initial handshake.

### Types of SSL Certificates

- **Domain Validated (DV)**: Validates the domain ownership.
- **Organization Validated (OV)**: Validates the domain ownership and organization information.
- **Extended Validation (EV)**: Provides the highest level of validation, showing the organization's name in the browser's address bar.

### Benefits of SSL

- **Security**: Encrypts sensitive information, such as login credentials and credit card information.
- **Trust**: Builds trust with users by showing that the website is secure.
- **SEO**: Google gives a slight ranking boost to websites using HTTPS.

## Transition from SSL to TLS

It's important to note that SSL has been succeeded by **TLS** (Transport Layer Security), which is more secure. When people refer to SSL today, they usually mean TLS.

## Enabling HTTPS with SSL/TLS

1. **Obtain an SSL/TLS Certificate**: Purchase or get a free SSL/TLS certificate from a trusted Certificate Authority (CA) like Let's Encrypt.
2. **Install the Certificate**: Install the certificate on your web server.
3. **Configure the Server**: Update your web server configuration to use the installed certificate.
4. **Update Your Website**: Ensure that your website is accessible via HTTPS, and update all internal links to use HTTPS.

## Resources

- **Let's Encrypt**: [https://letsencrypt.org/](https://letsencrypt.org/)
- **SSL Labs**: [https://www.ssllabs.com/](https://www.ssllabs.com/)
- **Mozilla Developer Network (MDN)**: [HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP/HTTPS)

## Conclusion

HTTPS and SSL/TLS are essential for securing online communications. By encrypting data and verifying the integrity and authenticity of websites, these technologies protect users from various types of cyber threats. Transitioning to HTTPS is crucial for maintaining security, trust, and SEO rankings in today's internet landscape.
