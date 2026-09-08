# Deployment Checklist

Use this checklist as the field summary for an ORIGIN deployment. It does not replace the detailed procedures in the rest of this chapter; it provides a compact acceptance sequence for the installation team.

The deployment should stop if a critical safety, heritage-protection, power, or system-health issue is discovered.

## 1. Site approval

- [ ] Monitoring objective is documented.
- [ ] Final mounting location is approved.
- [ ] Mounting method is approved by the site authority.
- [ ] Installation does not require unapproved intervention in historic material.
- [ ] Visitor and staff access are considered.
- [ ] Maintenance access is possible.
- [ ] Power source is defined.
- [ ] Connectivity method is defined or offline operation is intentional.
- [ ] Solar exposure has been assessed where applicable.
- [ ] Sensor directions have been planned.

## 2. Unit identification

- [ ] ORIGIN unit ID recorded.
- [ ] Rosetta hardware revision recorded.
- [ ] Enclosure/mechanical revision recorded.
- [ ] Firmware version recorded.
- [ ] Deployment configuration version recorded.
- [ ] Enabled modules recorded.
- [ ] Calibration/model version recorded where relevant.

## 3. Pre-installation hardware inspection

- [ ] Enclosure has no transport damage.
- [ ] Fasteners and mounting hardware are complete.
- [ ] Rosetta is securely mounted.
- [ ] Internal cables are restrained.
- [ ] Sensor openings are unobstructed.
- [ ] C4001 radar boards are secure and correctly oriented.
- [ ] Seals/gaskets are undamaged.
- [ ] Solar supports and cable path are intact where used.
- [ ] No loose parts remain inside the enclosure.

## 4. Physical installation

- [ ] Unit is installed at the approved location.
- [ ] Mounting is stable with no unacceptable movement.
- [ ] Installation is reversible where required.
- [ ] Radar A/B/C directions are documented.
- [ ] BIT interface remains accessible.
- [ ] Service panels can still be opened.
- [ ] Cables are protected and strain-relieved.
- [ ] No cable creates a trip hazard.
- [ ] No sharp edge or protrusion is exposed to visitors.
- [ ] Installation does not obstruct paths or emergency access.

## 5. Solar and power

- [ ] Solar panel is securely mounted where used.
- [ ] Solar orientation matches the site plan.
- [ ] Cable is routed through the intended protected path.
- [ ] Cable is not pinched or sharply bent.
- [ ] Power polarity and connectors are verified.
- [ ] No exposed conductors are present.
- [ ] Initial power-up is stable.
- [ ] No repeated resets, abnormal heating, smell, or unexpected current behavior is observed.

## 6. Sealing and enclosure

- [ ] Gaskets are correctly seated.
- [ ] Enclosure seams are fully closed.
- [ ] Cable penetrations are secured.
- [ ] Sensor openings match the intended design.
- [ ] Solar cable entry is protected.
- [ ] Final enclosure photographs are taken.

## 7. Startup and setup

- [ ] Unit boots normally.
- [ ] Unit identity matches the deployment record.
- [ ] Expected sensors are detected.
- [ ] Expected modules are detected.
- [ ] Correct configuration is loaded.
- [ ] Configuration has been read back and verified.
- [ ] Local storage is detected and writable.
- [ ] Time/timestamps are valid.
- [ ] Device health state is available.
- [ ] No critical startup fault remains unresolved.

## 8. Communications

- [ ] Intended communication interface initializes.
- [ ] Network attachment succeeds where required.
- [ ] Upstream service is reachable where required.
- [ ] Authentication succeeds.
- [ ] Test data is received by the intended upstream system.
- [ ] Loss of connectivity is visible as a health state.
- [ ] Offline/local buffering works where required.
- [ ] Reconnection behavior has been checked.

## 9. Calibration

- [ ] Baseline site behavior has been observed.
- [ ] Radar A has been tested across its intended zone.
- [ ] Radar B has been tested across its intended zone.
- [ ] Radar C has been tested across its intended zone.
- [ ] Known blind zones are documented.
- [ ] Known false-detection sources are documented.
- [ ] Environmental readings are plausible.
- [ ] Reference comparisons are recorded where performed.
- [ ] Thresholds/rules are documented.
- [ ] Multi-sensor event behavior has been checked.

## 10. Commissioning

- [ ] Final physical inspection passes.
- [ ] Stable operation on the real power source is confirmed.
- [ ] Every required sensor generates valid data.
- [ ] At least one controlled presence/event test is traced end to end.
- [ ] Local event storage is verified.
- [ ] Upstream event delivery is verified where applicable.
- [ ] Controlled restart succeeds.
- [ ] Configuration survives restart.
- [ ] Sensor health recovers after restart.
- [ ] Communications recover after restart.
- [ ] At least one safe fault condition has been verified where practical.
- [ ] Sensor failure is not represented as a normal zero/no-presence value.

## 11. Centaurus AI / decision layer

If Centaurus is active:

- [ ] Model/rule version is recorded.
- [ ] Input sources are known.
- [ ] Confidence and severity are presented separately.
- [ ] Supporting observations can be traced.
- [ ] Known limitations are documented.
- [ ] Operator review process is defined.
- [ ] No unapproved autonomous action is enabled.

## 12. Documentation

- [ ] Site assessment is complete.
- [ ] Installation photographs are stored.
- [ ] Final orientation map is stored.
- [ ] Configuration version is recorded.
- [ ] Calibration results are stored.
- [ ] Commissioning results are stored.
- [ ] Known limitations are stored.
- [ ] Maintenance owner/contact is recorded.
- [ ] Removal/rollback method is documented.

## 13. Handover

- [ ] Site operator knows the unit ID.
- [ ] Normal health state has been explained.
- [ ] Degraded and fault states have been explained.
- [ ] Power-loss response has been explained.
- [ ] Communications-loss response has been explained.
- [ ] Sensor-fault escalation has been explained.
- [ ] Maintenance access restrictions are understood.
- [ ] Support/escalation contact is known.

## Final acceptance

Select one outcome:

- [ ] **Accepted** — all required functions pass.
- [ ] **Accepted with limitations** — usable with documented non-critical limitations.
- [ ] **Rework required** — issues must be corrected before operation.
- [ ] **Rejected / rollback** — deployment should not enter normal operation.

### Deployment sign-off

| Field | Value |
| --- | --- |
| Site | |
| Unit ID | |
| Date | |
| Hardware revision | |
| Firmware version | |
| Configuration version | |
| Commissioning result | |
| Outstanding limitations | |
| Team representative | |
| Site representative | |

Once accepted, continue with the operational guidance under [Maintenance](../maintenance/README.md) and record real deployments under [Deployments](../deployments/README.md).