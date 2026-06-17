# Managing Workspace Seats

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Managing Workspace Seats**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling subscription tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Inviting users, purchasing additional seats, and deleting inactive accounts.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Navigate to the Members tab in workspace configurations.** - Navigate to the Members tab in workspace configurations.
2. **Click 'Add Seat' to open billing cart.** - Click 'Add Seat' to open billing cart.
3. **Confirm the unit seat price change ($15/seat/month).** - Confirm the unit seat price change ($15/seat/month).
4. **Input the invitation email address of the team member.** - Input the invitation email address of the team member.
5. **Select workspace role tier and click Send Invite.** - Select workspace role tier and click Send Invite.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Invite link expired
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Invitation confirmation links are active for 72 hours. You can trigger a link dispatch via the 'Resend Invitation' button.

## Frequently Asked Questions

### Q: Do I get billed for pending invites?
**A**: Yes, billing is based on active allocated seats, regardless of whether the invited user has completed their registration.

## Related Articles

- [Role-Based Access Control Mapping](../subscription/role_based_access_control_mapping.md)
- [Downgrading Plan Consequences](../subscription/downgrading_plan_consequences.md)
