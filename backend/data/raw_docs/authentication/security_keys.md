# Hardware Security Keys Support

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Hardware Security Keys Support**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling authentication tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Adding FIDO2, YubiKey, or built-in biometric security systems to your CloudFlow account.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Navigate to Account Settings > Security panel.** - Navigate to Account Settings > Security panel.
2. **Scroll down to 'Hardware Key Authentication' and click 'Register Security Key'.** - Scroll down to 'Hardware Key Authentication' and click 'Register Security Key'.
3. **Verify your identity by entering your current account password.** - Verify your identity by entering your current account password.
4. **Plug your security key into your USB port (or hold it near your NFC reader).** - Plug your security key into your USB port (or hold it near your NFC reader).
5. **Touch the contact button on the security key when prompted by your browser.** - Touch the contact button on the security key when prompted by your browser.
6. **Name the device (e.g., 'Primary YubiKey 5C') and save settings.** - Name the device (e.g., 'Primary YubiKey 5C') and save settings.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Key registration failing on Safari
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Verify that your key supports WebAuthn protocols and that you are using Safari version 13 or higher.

## Frequently Asked Questions

### Q: Can I register multiple hardware keys?
**A**: Yes, we strongly recommend registering at least one backup key in case your primary key is misplaced.

## Related Articles

- [Two-Factor Authentication Setup](../authentication/two_factor_authentication_setup.md)
- [Password Complexity Policies](../authentication/password_complexity_policies.md)
