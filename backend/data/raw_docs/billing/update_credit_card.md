# Updating Credit Card Details

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Updating Credit Card Details**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling billing tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: How to modify payment details, change primary credit cards, and clear stale card profiles.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Go to Organization Settings > Billing panel.** - Go to Organization Settings > Billing panel.
2. **Click 'Update Payment Method' in the billing card section.** - Click 'Update Payment Method' in the billing card section.
3. **Fill in card number, expiration date, security code (CVV), and billing address.** - Fill in card number, expiration date, security code (CVV), and billing address.
4. **Authorize verification check from your banking app if triggered.** - Authorize verification check from your banking app if triggered.
5. **Set the newly created card as the Primary payment method.** - Set the newly created card as the Primary payment method.
6. **Delete any legacy credit cards to avoid future billing errors.** - Delete any legacy credit cards to avoid future billing errors.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ Postal code verification error
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Verify that the billing zip/postal code entered matches the address registered with your bank exactly.

## Frequently Asked Questions

### Q: Are credit card details saved on CloudFlow systems?
**A**: No, all card information is sent directly to Stripe using PCI-compliant tokens. We never store raw credit card credentials.

## Related Articles

- [Managing Card Declines](../billing/managing_card_declines.md)
- [Self-Service Billing Portal](../billing/self_service_billing_portal.md)
