# Bauplan Bus Analyzer

Install:

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Create a new branch:

```
bauplan branch create <user>.bbus
bauplan branch checkout <user>.bbus
```

Create a snapshot of the current GTFS files for Madison Metro:

```
cd pipelines
bauplan run -p snapshot_routes
bauplan run -p current_routes
bauplan query "SELECT unix_timestamp, source FROM route_snapshots"
```

Merge back to main branch:

```
bauplan branch checkout main
bauplan branch merge <user>.bbus
```
