# Managing Card Declines

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Managing Card Declines**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling billing tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Resolving payment failure notifications, automatic retry schedules, and grace intervals.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

## Deep Technical Insights
### Transaction Processing & Financial Integrity
All financial transactions on the CloudFlow platform are handled via Stripe, utilizing payment card industry data security standards (PCI-DSS) Level 1 compliance structures. Sensitive credit card digits never touch CloudFlow servers. Instead, card data is directly serialized at the browser level and exchanged for secure Stripe tokens.

### Proration Arithmetic & Billing Calculations
When plans are modified, added seats, or upgraded mid-cycle, CloudFlow automatically computes prorated charges down to the exact second. The calculation uses the formula: `Prorated Charge = (Days Remaining / Days in Billing Cycle) * (New Plan Rate - Old Plan Rate)`. This ensures customers only pay for resources that they actively allocate. Any calculated credit offsets are stored as promotional credit balances and applied to subsequent monthly or annual invoice statements.

### Standard Billing Account Lifecycle States
- **Active**: Card successfully charged, all system integrations and workflow runs operating within bounds.
- **Past Due**: The primary charge card declined. Workflows continue executing during a 14-day grace interval.
- **Unpaid**: All retry attempts failed. Automated execution runs are suspended; database files are preserved in read-only hibernation mode.
- **Canceled**: Subscription terminated at user request. The account preserves access until the end of the paid cycle.

## Step-by-Step Instructions

1. **Locate the payment decline notification email from CloudFlow.** - Locate the payment decline notification email from CloudFlow.
2. **Identify the error code returned by your bank (e.g. 'insufficient_funds', 'authentication_required').** - Identify the error code returned by your bank (e.g. 'insufficient_funds', 'authentication_required').
3. **Log into the billing portal and click 'Update Payment Method'.** - Log into the billing portal and click 'Update Payment Method'.
4. **Enter your card information and pass the 3D Secure verification check.** - Enter your card information and pass the 3D Secure verification check.
5. **Click 'Retry Payment' to retry the outstanding invoice immediately.** - Click 'Retry Payment' to retry the outstanding invoice immediately.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Payment retry fails repeatedly
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Ensure that your credit card is authorized for international online transactions. CloudFlow processing is handled in the United States.

## Frequently Asked Questions

### Q: What is the retry schedule for unpaid invoices?
**A**: Stripe retries failed invoice charges on Day 1, Day 3, Day 7, and Day 14. If payment is not secured by Day 14, the workspace is locked.

### Q: Can I add a backup payment card?
**A**: Yes, you can register multiple cards in the portal and mark one as the Primary payment method and the others as Backup methods.

## Related Articles

- [Updating Credit Card Details](../billing/updating_credit_card_details.md)
- [Invoice History Management](../billing/invoice_history_management.md)
