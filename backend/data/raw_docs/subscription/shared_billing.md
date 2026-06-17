# Creating Unified Workspace Profiles

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Creating Unified Workspace Profiles**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling subscription tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Consolidating billing for multiple distinct company sub-accounts under one primary billing profile.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

## Deep Technical Insights
### Subscription Tiers & Scale Limits
CloudFlow structures subscription tiers to balance resource limits and run quotas for teams of different sizes. Starter packages are ideal for simple automation, while Professional and Enterprise tiers scale to high-volume corporate tasks.

### Dynamic Seat Allocation System
Workspace seat management operates on a concurrent user allocation model. Adding a new user seat invites a colleague to register their credentials, immediately updating the active team directory list. If the team size exceeds active subscription allocations, the billing layer appends the new seat unit price ($15/seat/month) to the pending billing cart. Removing an active seat releases the allocated resource, returning it to the pool of unused seats. A seat can be deleted completely from the console settings to decrease recurring base subscription fees permanently.

### Detailed Plan Quotas Breakdown
| Limit Type | Starter Plan | Professional Plan | Enterprise Plan |
| :--- | :--- | :--- | :--- |
| Active Workflows | Max 10 flows | Unlimited | Unlimited (Dedicated Runs) |
| Monthly Executions | 1,000 runs | 50,000 runs | Custom (Multi-million capacity) |
| Data Retention Log | 7 days logs | 90 days logs | 7 years logs (Audit Compliant) |
| Concurrency Limit | 2 concurrent runs | 10 concurrent runs | 50+ concurrent runs (Scalable) |

## Step-by-Step Instructions

1. **Access the parent organization dashboard.** - Access the parent organization dashboard.
2. **Navigate to Organization Settings > Sub-Accounts Billing.** - Navigate to Organization Settings > Sub-Accounts Billing.
3. **Link target child workspace IDs.** - Link target child workspace IDs.
4. **Save settings to process unified consolidated payments.** - Save settings to process unified consolidated payments.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Frequently Asked Questions

### Q: Are itemized invoices separated?
**A**: Yes, the main receipt breaks down usage costs and run details for each workspace individually.

## Related Articles

- [Self-Service Billing Portal](../subscription/self_service_billing_portal.md)
- [Logging into Multiple Organizations](../subscription/logging_into_multiple_organizations.md)
