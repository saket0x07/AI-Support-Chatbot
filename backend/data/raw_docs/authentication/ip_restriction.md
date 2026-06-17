# Setting Login IP Restrictions

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Setting Login IP Restrictions**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling authentication tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Limiting console access to authorized corporate network environments and VPN CIDR blocks.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

## Deep Technical Insights
### Architectural Details & Security Standards
CloudFlow's authentication layer is built upon industry-standard OAuth 2.0 and SAML 2.0 specifications. Passphrases are salted and hashed using the Argon2id encryption algorithm with parameters configured to prevent GPU-based brute-force attacks. Authentication sessions emit stateless JSON Web Tokens (JWTs) cryptographically signed using RS256 keys. These tokens contain standardized claim parameters (such as `iss`, `sub`, `exp`, and custom organization role memberships) to govern RBAC policies. To safeguard access, all tokens are validated on a per-request basis against our centralized caching layer (powered by Redis) to ensure revocation status is evaluated in real-time.

### Security Key WebAuthn Standards
Hardware token authentications use WebAuthn protocols under FIDO2 rules. This eliminates the susceptibility to credential-harvesting phishing campaigns by leveraging public-key cryptography. When registering YubiKeys or local biometrics, the device creates a unique public/private key pair. The public key is stored securely on the CloudFlow user directory database, while the private key remains locked on the physical device secure enclave. Authentication challenges require a touch or biometric verification to decrypt the challenge token and authorize the request.

### Custom Organization Security Policies Config
| Parameter | Starter Tier | Professional Tier | Enterprise Tier |
| :--- | :--- | :--- | :--- |
| Max Session Idle Time | Fixed (24 hours) | Configurable (1h - 24h) | Configurable (15m - 24h) |
| Password Expiration | Disabled | Optional (90 days) | Configurable (30 - 365 days) |
| SSO / SAML / Okta | Not Available | Not Available | Supported (Fully Enforceable) |
| IP Whitelisting | Not Available | Not Available | Supported (CIDR Ranges) |

## Step-by-Step Instructions

1. **Open Security Settings inside the Enterprise console.** - Open Security Settings inside the Enterprise console.
2. **Find the 'IP Access Control List (ACL)' policy section.** - Find the 'IP Access Control List (ACL)' policy section.
3. **Toggle ACL control from Disabled to Enforced.** - Toggle ACL control from Disabled to Enforced.
4. **Enter the list of authorized IPv4/IPv6 CIDR ranges (e.g., 192.168.1.0/24).** - Enter the list of authorized IPv4/IPv6 CIDR ranges (e.g., 192.168.1.0/24).
5. **Add a label to identify each block (e.g., 'London Corporate Office VPN').** - Add a label to identify each block (e.g., 'London Corporate Office VPN').
6. **Click Save to activate restrictions. Any sessions originating from untrusted IPs will be closed.** - Click Save to activate restrictions. Any sessions originating from untrusted IPs will be closed.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Accidental owner lockout
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: If you lock yourself out by entering incorrect IP definitions, contact CloudFlow Enterprise support to run out-of-band identity checks.

## Frequently Asked Questions

### Q: Does IP restriction impact workflow runner calls?
**A**: No. IP restrictions only govern access to the web management dashboard, not API endpoints.

## Related Articles

- [Integrating SAML SSO with Okta](../authentication/integrating_saml_sso_with_okta.md)
- [Audit Logs Reference Guide](../authentication/audit_logs_reference_guide.md)
