# Outage Response Protocol

This runbook details procedures for handling connectivity or power outages affecting edge nodes or data relay systems.

## Triggers

- Heartbeat failure from node > 3 mins.
- Missing Starlink uplink confirmations.
- Cloud alert: "Zone X Offline"

## Steps

1. **Detect**
- Monitor from Node Heartbeat Dashboard.
- Identify affected zone and node ID.

2. **Diagnose**
- Run remote diagnostics (`./diag --ping --modem`)
- Determine if power or link is root cause.

3. **Respond**
- Auto-switch to LTE uplink if Starlink fails.
- Dispatch drone relay if LTE also fails.
- Notify IC if backup systems also down.

4. **Restore**
- Reboot node remotely or on-site.
- Validate with `./connectivity_check.sh`.

## Metrics

- MTTR: < 15 mins.
- Resilience target: 99.7% uptime/node.

