# Adding Billing Contacts

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Adding Billing Contacts**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling billing tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: How to register accounting emails to receive automated PDF invoices and alerts.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Go to the Billing control tab.** - Go to the Billing control tab.
2. **Find the 'Billing Notifications Contacts' table.** - Find the 'Billing Notifications Contacts' table.
3. **Click 'Add Contact Email'.** - Click 'Add Contact Email'.
4. **Enter the name and email address of your accounting representative.** - Enter the name and email address of your accounting representative.
5. **Save contacts list updates.** - Save contacts list updates.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Accounting contacts not receiving emails
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Ensure that your accounting inbox doesn't filter out automated emails dispatched from billing@cloudflow.com.

## Frequently Asked Questions

### Q: Can billing contacts log into the dashboard workspace?
**A**: No. Billing contacts only receive invoice files via email and cannot access workspace directories unless they are explicitly invited as workspace members.

## Related Articles

- [Invoice History Management](../billing/invoice_history_management.md)
- [Role-Based Access Control Mapping](../billing/role_based_access_control_mapping.md)
