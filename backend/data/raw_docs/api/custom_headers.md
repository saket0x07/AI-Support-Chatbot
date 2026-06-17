# Custom API Headers Reference

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Custom API Headers Reference**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling api tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Sending metadata tracking headers, environment flags, and tracking IDs.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Append custom tracking tags in request header structures.** - Append custom tracking tags in request header structures.
2. **Use `X-CloudFlow-Environment` to specify test vs production flow runs.** - Use `X-CloudFlow-Environment` to specify test vs production flow runs.
3. **Use `X-Correlation-ID` to track request steps through system logging streams.** - Use `X-Correlation-ID` to track request steps through system logging streams.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Frequently Asked Questions

### Q: Are headers preserved in webhook responses?
**A**: Yes, custom headers configured in your flows are returned in related webhook payloads.

## Related Articles

- [Configuring Outbound Webhooks](../api/configuring_outbound_webhooks.md)
- [Idempotent API Operations](../api/idempotent_api_operations.md)
