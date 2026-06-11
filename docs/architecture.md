# System Architecture

## Workflow

Waste Level Data

↓

Distance Measurement

↓

Fill Percentage Calculation

↓

Status Classification

↓

Alert Generation

↓

CSV Logging

↓

Dashboard Visualization

↓

PDF Report Generation

↓

Collection Decision

---

## Architecture Diagram

+--------------------+

| Waste Bin |

+----------+---------+

|

v

+--------------------+

| Distance Sensor |

| (Simulated) |

+----------+---------+

|

v

+--------------------+

| Bin Monitor |

+----------+---------+

|

v

+--------------------+

| Fill Percentage |

| Calculator |

+----------+---------+

|

v

+--------------------+

| Alert Manager |

+----------+---------+

|

v

+--------------------+

| Data Logger |

+----------+---------+

|

v

+--------------------+

| Dashboard |

+----------+---------+

|

v

+--------------------+

| Report Generator |

+--------------------+

---

## Core Modules

### simulator.py

Generates virtual sensor data.

### bin_monitor.py

Calculates fill percentage.

### alert_manager.py

Triggers alerts.

### data_logger.py

Stores monitoring history.

### dashboard_generator.py

Creates dashboard visualizations.

### report_generator.py

Generates PDF reports.
