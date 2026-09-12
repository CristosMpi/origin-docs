# Site Assessment

A reliable ORIGIN deployment begins before any hardware is installed. The site assessment determines whether the selected location can support the required sensing, power, communications, mounting, maintenance, and operational goals.

The purpose of the assessment is not to force ORIGIN into a predetermined location. It is to understand the location well enough to choose a deployment that is technically useful, physically safe, and acceptable to the site authority.

## Assessment objectives

The assessment should answer five basic questions:

1. **What needs to be monitored?**
2. **Where can the unit be mounted safely?**
3. **Will the sensors have useful coverage?**
4. **Can the unit be powered and connected reliably?**
5. **Can the installation be maintained without harming the site?**

If any of these questions cannot be answered, the deployment design is not yet complete.

## Define the monitoring objective

Before choosing a mounting point, define what the deployment is trying to observe.

Examples may include environmental conditions around an artifact or area; human presence in a monitored zone; movement near a restricted area; local physical changes or anomalies; and data collection for a pilot study.

Different objectives can require different sensor directions, mounting heights, distances, and operating thresholds.

## Document the physical environment

Record the area using sketches, photographs, dimensions, and notes.

Useful information includes walls, columns, display structures, fences, paths, and entrances; likely visitor movement; nearby electrical equipment; metal structures and large reflective surfaces; vegetation or moving objects; areas exposed to rain, splash, dust, or direct sun; possible locations for solar exposure; accessible maintenance routes; and restrictions imposed by the museum or archaeological authority.

For sensitive heritage environments, photographs and location records should be stored according to the institution's policies.

## Mounting assessment

The selected mounting location must support both structural stability and the monitoring objective.

Check whether the support surface is stable; whether drilling or permanent fasteners are permitted; whether a reversible mounting method can be used; whether the unit can be reached for maintenance; whether visitors can touch or interfere with it; whether the unit obstructs paths or emergency routes; whether cables can be routed safely; and whether the tall enclosure is exposed to accidental impact or overturning.

A mounting point that gives excellent sensor coverage but is unsafe or unacceptable to the site should be rejected.

## mmWave assessment

The current ORIGIN Core concept uses multiple DFRobot C4001 mmWave sensors. Radar placement should therefore be assessed in the real geometry of the location.

Consider intended sensor directions; likely target approach paths; walls or barriers inside the expected field of view; nearby moving objects; reflective metal surfaces; areas behind the sensor openings; possible overlap between the three radars; and likely blind zones.

Do not assume that three sensors automatically provide complete 360-degree coverage. The final coverage must be measured during calibration and commissioning.

## Environmental sensing assessment

Environmental sensors can be strongly affected by mounting location.

Avoid positions where a sensor intended to represent the local environment is dominated by direct solar heating; warm electronics exhaust; air-conditioning outlets; enclosed dead-air pockets; water splash; heat radiating from a wall or display light; and nearby equipment that does not represent the monitored environment.

The selected position should match the meaning of the measurement.

## Solar assessment

If solar power is used, inspect the location across the expected operating period.

Record direction of available sunlight; major sources of shade; seasonal changes likely to affect exposure; nearby trees, walls, roofs, or monuments; whether the solar panel can be oriented without interfering with site appearance or access; and cable route from the panel through the hollow support into ORIGIN Core.

A short inspection at one time of day is not enough to prove adequate year-round solar availability.

## Power assessment

Determine the intended power source and its constraints.

For wired power, confirm outlet or supply location; cable length; cable protection; voltage compatibility; risk of accidental disconnection; and whether temporary extensions are acceptable.

For battery/solar operation, confirm expected energy budget, charging opportunity, access for battery maintenance, and expected periods without usable sunlight.

The power design should be validated separately from the visual suitability of the mounting point.

## Connectivity assessment

The location should be checked for the actual communications method intended for the deployment.

Depending on the implementation, this may include Wi-Fi coverage; cellular signal; wired networking; local gateway communication; and offline/local-only operation.

Record signal conditions at the exact mounting position rather than elsewhere in the building or site.

Connectivity should be classified separately from basic device health. ORIGIN must still distinguish a healthy but offline device from a failed device.

## Privacy and visitor considerations

Presence monitoring can affect how a deployment is perceived even when no camera is used.

The assessment should therefore consider whether the monitored zone includes public visitor areas; what data will be stored; whether presence events can be linked to individuals; retention requirements; required signage or institutional approval; and who can access the data.

The deployment should collect only what is needed for the stated monitoring objective.

## Maintenance assessment

Ask how the unit will be serviced after the installation team leaves.

Confirm access to fasteners and service panels; access to the BIT interface where used; whether the enclosure can be opened without moving heritage objects; whether the solar panel can be cleaned or inspected; whether sensors can be replaced; whether technicians can work safely at the mounting height; and how the device can be removed if required.

A deployment that cannot be maintained is not a complete deployment design.

## Site assessment record

A site assessment record should include:

| Item | Record |
| --- | --- |
| Site | Name and location |
| Assessment date | Date |
| Assessed by | Team / site personnel |
| Monitoring objective | Short description |
| Candidate mounting point | Description / drawing |
| Power | Method and constraints |
| Connectivity | Method and measured condition |
| Radar directions | Proposed orientation |
| Environmental risks | Heat, rain, dust, splash, etc. |
| Heritage restrictions | Approved / prohibited methods |
| Maintenance access | Yes / no / limitations |
| Open issues | Items requiring resolution |
| Decision | Accept / revise / reject |

## Acceptance criteria

A candidate location should move to installation only when the monitoring objective is clear; a safe mounting strategy exists; required site approval has been obtained; power is feasible; connectivity is feasible or offline operation is intentionally supported; sensor positioning is physically possible; maintenance access exists; and no unresolved heritage-protection issue blocks the installation.

The next step is [Installation](installation.md).
