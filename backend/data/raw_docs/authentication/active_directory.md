# Active Directory Integration Settings

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Active Directory Integration Settings**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling authentication tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Syncing corporate directory groups with CloudFlow workspaces using LDAP protocols.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Access the organization administration page.** - Access the organization administration page.
2. **Navigate to Settings > Directory Sync.** - Navigate to Settings > Directory Sync.
3. **Select 'Active Directory (LDAP)' as the source provider.** - Select 'Active Directory (LDAP)' as the source provider.
4. **Specify your LDAP Server URL (e.g., ldaps**//directory.company.com
5. **Enter the Bind DN credentials for a read-only sync agent.** - Enter the Bind DN credentials for a read-only sync agent.
6. **Map LDAP groups (e.g., CN=Engineering,OU=Groups) to CloudFlow workspace roles.** - Map LDAP groups (e.g., CN=Engineering,OU=Groups) to CloudFlow workspace roles.
7. **Test connection and initiate the initial user sync execution.** - Test connection and initiate the initial user sync execution.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ LDAP connection timeout
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Verify that your local firewall permits ingress requests from CloudFlow static IP addresses listed in the networking document.

### ⚠️ User synchronization skips specific employees
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Ensure target accounts have both 'mail' and 'displayName' parameters populated in the LDAP system.

## Frequently Asked Questions

### Q: How frequently does the active directory sync run?
**A**: Sync runs automatically every 60 minutes. Administrators can trigger a manual sync run using the 'Sync Now' button.

### Q: What happens when an employee is disabled in Active Directory?
**A**: Their CloudFlow session will be terminated immediately, and their workspace seats will be set to suspended.

## Related Articles

- [Integrating SAML SSO with Okta](../authentication/integrating_saml_sso_with_okta.md)
- [Role-Based Access Control Mapping](../authentication/role_based_access_control_mapping.md)
