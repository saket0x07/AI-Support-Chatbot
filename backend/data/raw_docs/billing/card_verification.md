# Resolving 3D Secure Verification Issues

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Resolving 3D Secure Verification Issues**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling billing tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Troubleshooting multi-factor authentication steps during credit card authorization processes.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

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

1. **Ensure you are attempting payment on a 3DS secure-compliant checkout page.** - Ensure you are attempting payment on a 3DS secure-compliant checkout page.
2. **Wait for the card provider's security modal to load in the browser.** - Wait for the card provider's security modal to load in the browser.
3. **Enter the authentication token code dispatched to your phone or banking app.** - Enter the authentication token code dispatched to your phone or banking app.
4. **Do not refresh or close the page while the payment status loads.** - Do not refresh or close the page while the payment status loads.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ 3D Secure modal fails to pop up
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Temporarily deactivate pop-up blockers or active ad-blockers inside your browser, as they regularly block bank authentication overlays.

## Frequently Asked Questions

### Q: Why is my card flagged for 3D Secure validation?
**A**: SCA (Strong Customer Authentication) mandates 3DS for European Union cards to safeguard accounts from fraud.

## Related Articles

- [Managing Card Declines](../billing/managing_card_declines.md)
- [Updating Credit Card Details](../billing/updating_credit_card_details.md)
