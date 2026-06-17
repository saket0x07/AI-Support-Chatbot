# API Access Key Generation

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **API Access Key Generation**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling api tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: How to generate API keys, assign scopes, and rotate production tokens safely.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

## Deep Technical Insights
### REST API Technical Specifications
The CloudFlow REST API is fully modeled using JSON payloads over standard HTTPS routes. Security verification is enforced on all incoming calls using standard bearer authorization keys. All endpoints support CORS pre-flight constraints and enforce payload checks using Pydantic validator modules.

### Rate Limiting Token Bucket Algorithm
To maintain backend stability, API queries are throttled using the token bucket algorithm. Each client namespace is allocated a token bucket with a fixed capacity. Every HTTP request consumes a single token. Tokens are replenished at a steady rate. When the bucket is empty, subsequent queries receive an HTTP 429 Too Many Requests response. The limits vary by tier: 60 queries/minute for Starter and 1,000 queries/minute for Professional profiles.

### HTTP Headers Reference Table
| Header Name | Type | Description |
| :--- | :--- | :--- |
| `Authorization` | String | Bearer token format: `Bearer CF_API_KEY_XXXX` |
| `Content-Type` | String | Must be set to `application/json` for POST/PUT requests |
| `Idempotency-Key` | String (UUID) | Prevents duplicate operations on network retries |
| `X-Correlation-ID` | String | Distributed tracking key passed across log records |

## Step-by-Step Instructions

1. **Navigate to the Developer Console (settings > Developer Console).** - Navigate to the Developer Console (settings > Developer Console).
2. **Go to the 'API Access Keys' tab and select 'Generate New Key'.** - Go to the 'API Access Keys' tab and select 'Generate New Key'.
3. **Provide a descriptive label for the token (e.g. 'Stripe Webhook Sync').** - Provide a descriptive label for the token (e.g. 'Stripe Webhook Sync').
4. **Define scopes** choose read-only or read/write access for workflows and database endpoints.
5. **Click Generate. Copy the generated key immediately and save it in a secure locker.** - Click Generate. Copy the generated key immediately and save it in a secure locker.
6. **Note** The API key will not be displayed again for security purposes.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Unauthorized (401) errors
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Ensure you are sending the API key inside the HTTP headers as 'Authorization: Bearer <API_KEY>' and that the token has not been revoked.

## Frequently Asked Questions

### Q: Can I configure expiration limits for API keys?
**A**: Yes, we support configuring keys with custom lifecycles ranging from 30 days to never-expires during creation.

### Q: Is there a limit to the number of active API keys?
**A**: Starter plans are limited to 3 active API keys. Professional and Enterprise tiers support unlimited active keys.

## Related Articles

- [API Rate Limiting Policies](../api/api_rate_limiting_policies.md)
- [Idempotent API Operations](../api/idempotent_api_operations.md)
