# Investigating Missing Triggers

## Overview
This official CloudFlow knowledge base article provides an in-depth reference for **Investigating Missing Triggers**. CloudFlow is a next-generation workflow orchestration and data routing platform designed for cloud-native businesses. Handling troubleshooting tasks securely and efficiently is a fundamental requirement of our systems. Whether you are configuring these policies in the web management dashboard or calling them programmatically via our API layer, this guide covers all relevant configuration steps, security validation details, and execution logic.

Specifically, this module manages the following requirements: Troubleshooting when automated workflows fail to fire upon external actions.. Under standard operations, these mechanisms are monitored for response latency, throughput, and error rates using our system telemetry engine. Administrators and developer profiles should read the permissions guidelines below to ensure proper authorization credentials.

## Deep Technical Insights
### Debugging Diagnostics & Logging
Resolving complex integration anomalies requires a structured approach to inspecting execution logs. CloudFlow dashboards display detailed diagnostics for every step run. You can click on any failed task block to inspect the raw JSON input payloads, headers, and specific error codes returned.

### System Network Routing & Whitelisting
If your automations are unable to query your internal endpoints (such as PostgreSQL databases or local CRM systems), the issue is likely due to corporate firewall policies blocking external networks. Ensure that you register CloudFlow's static egress IP addresses in your router access control lists (ACLs). The active egress IP addresses are: `34.120.45.1` and `34.120.45.2`. Using strict SSL checks is also highly recommended; however, you can deactivate strict checks inside custom HTTP cards during debugging runs.

### Step-by-Step Recovery Checklist
1. **Access Logs**: Go to Flow Telemetry and filter runs showing status='Failed'.
2. **Verify Inputs**: Copy the output payload of the preceding step and confirm it matches the input schema of the failing step.
3. **Validate Auth**: Check if the connected application credentials are active or if the token was revoked.
4. **Re-run Job**: Settle formatting issues and click 'Retry Run' to execute the failed queue item.

## Step-by-Step Instructions

1. **Check the 'Failed Triggers' log stream in your developer panel.** - Check the 'Failed Triggers' log stream in your developer panel.
2. **Verify endpoint connectivity using a manual trigger check command.** - Verify endpoint connectivity using a manual trigger check command.
3. **Review payload body shapes** make sure incoming JSON matches required parameters schema.
4. **Check authentication token expiration settings.** - Check authentication token expiration settings.

## Edge Cases & Advanced Configurations
Under standard operational paradigms, the CloudFlow pipeline handles concurrency gracefully. However, developers should design integration flows to handle extreme scenarios, such as network partitions, rate limit headers exceeding plan boundaries, or credentials revocation mid-run. If a run is stuck or encounters infinite loop thresholds (more than 100 consecutive loops), the monitoring engine automatically terminates the execution run, raising error code `ERR_LOOP_DETECTED`. For transactions, always utilize `Idempotency-Key` headers when retrying API POST requests to prevent creating duplicate invoices or database rows.

## Common Issues & Resolutions

### ⚠️ IP blocked by local firewall
**Description**: Encountered when system bounds or client validations fail.
**Resolution**: Register our static IP ranges listed in the developer documentation within your internal server whitelist rules.

## Frequently Asked Questions

### Q: Why is my webhook triggers log empty?
**A**: If empty, the source server failed to dispatch the request. Check your source service's outgoing webhook statistics.

## Related Articles

- [Configuring Outbound Webhooks](../troubleshooting/configuring_outbound_webhooks.md)
- [Resolving Workflow Timeouts](../troubleshooting/resolving_workflow_timeouts.md)
