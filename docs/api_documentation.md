# API Documentation

## WasteBinSimulator

### generate_record()

Returns:

{
"timestamp": "...",
"distance_cm": 10,
"fill_percentage": 75,
"status": "HALF FULL",
"alert": "Normal"
}

---

## BinMonitor

### calculate_fill_percentage(distance)

Input:

distance = 10

Output:

75

---

### get_status(fill_percentage)

Returns:

EMPTY

HALF FULL

FULL

---

## AlertManager

### get_alert(fill_percentage)

Returns:

{
"alert": true,
"message": "BIN FULL - COLLECTION REQUIRED"
}

---

## DataLogger

### log(record)

Stores records in CSV.

### read_logs()

Returns Pandas DataFrame.

---

## WasteReportGenerator

### generate_pdf()

Creates waste monitoring report.

---

## DashboardGenerator

### generate_chart()

Creates dashboard HTML visualization.
