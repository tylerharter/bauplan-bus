import bauplan
import time

GTFS_SOURCE = "http://transitdata.cityofmadison.com/GTFS/mmt_gtfs.zip"

@bauplan.model(
    internet_access=True,
    materialization_strategy='APPEND',
)
@bauplan.python('3.11', pip={
    'requests': '2.32.3', 'pandas': '2.0.3', 'numpy': '1.26.4'
})
def route_snapshots(data=bauplan.Model("titanic")):
    # use titanic table as dummy table because we don't actually want an input...
    import pandas as pd
    import requests

    download_path = "downloaded_gtfs.zip"
    r = requests.get(GTFS_SOURCE)
    r.raise_for_status()
    return pd.DataFrame([{
        "unix_timestamp": int(time.time()),
        "source": GTFS_SOURCE,
        "zip_contents": r.content
    }])
