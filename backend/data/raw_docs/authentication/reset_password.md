# Account Password Recovery

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Account Password Recovery**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling authentication tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: How to request a password reset, manage verification email expiration, and resolve security lockouts.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Navigate to the CloudFlow sign-in portal (auth.cloudflow.com).** - Navigate to the CloudFlow sign-in portal (auth.cloudflow.com).
2. **Click on the 'Forgot Password?' link located beneath the login credentials fields.** - Click on the 'Forgot Password?' link located beneath the login credentials fields.
3. **Input the email address registered with your CloudFlow organization account.** - Input the email address registered with your CloudFlow organization account.
4. **Click 'Send Recovery Email' and wait for the dispatch message.** - Click 'Send Recovery Email' and wait for the dispatch message.
5. **Open the recovery email in your inbox and click 'Reset Your Password' link.** - Open the recovery email in your inbox and click 'Reset Your Password' link.
6. **Define a new strong password complying with our character safety guidelines.** - Define a new strong password complying with our character safety guidelines.
7. **Confirm the changes and log in with your updated credentials.** - Confirm the changes and log in with your updated credentials.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ No email received
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Check your spam or junk folder. Verify that your organization is not blocking emails from notifications@cloudflow.com.

### ⚠️ Link expired error
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Password reset links are valid for exactly 15 minutes. If your link has expired, request a new reset from the forgot password page.

## Frequently Asked Questions

### Q: Can I reuse my previous password?
**A**: No. CloudFlow enforces a password history policy. You cannot reuse any of your last 5 passwords for security purposes.

### Q: How many times can I attempt to log in before my account is locked?
**A**: Accounts are locked after 5 consecutive failed login attempts. The lockout lasts 30 minutes, or you can unlock it via email reset immediately.

## Related Articles

- [Two-Factor Authentication Setup](../authentication/two_factor_authentication_setup.md)
- [Password Complexity Policies](../authentication/password_complexity_policies.md)
