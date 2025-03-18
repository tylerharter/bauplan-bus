import bauplan

def read_gtfs_feed(route_snapshots):
    import gtfs_kit as gk

    df = route_snapshots.to_pandas()
    df = df[df["unix_timestamp"] == df["unix_timestamp"].max()].reset_index()

    download_path = "downloaded_gtfs.zip"
    with open("downloaded_gtfs.zip", "wb") as f:
        f.write(df.at[0, "zip_contents"])
    feed = gk.read_feed(download_path, dist_units='m')
    return feed

    
@bauplan.model(
    materialization_strategy='REPLACE',
)
@bauplan.python('3.11', pip={
    'gtfs-kit': '5.0.2', 'geopandas': '0.14.4',
    'pandas': '1.5.3', 'numpy': '1.23.2'
})
def current_routes(data=bauplan.Model("route_snapshots")):
    feed = read_gtfs_feed(data)
    return feed.routes


@bauplan.model(
    materialization_strategy='REPLACE',
)
@bauplan.python('3.11', pip={
    'gtfs-kit': '5.0.2', 'geopandas': '0.14.4',
    'pandas': '1.5.3', 'numpy': '1.23.2'
})
def current_trips(data=bauplan.Model("route_snapshots")):
    trips = read_gtfs_feed(data).trips
    assert trips is not None
    return trips[["trip_id", "route_id", "service_id"]]


@bauplan.model(
    materialization_strategy='REPLACE',
)
@bauplan.python('3.11', pip={
    'gtfs-kit': '5.0.2', 'geopandas': '0.14.4',
    'pandas': '1.5.3', 'numpy': '1.23.2'
})
def current_stop_times(data=bauplan.Model("route_snapshots")):
    stop_times = read_gtfs_feed(data).stop_times
    assert stop_times is not None
    return stop_times


@bauplan.model(
    materialization_strategy='REPLACE',
)
@bauplan.python('3.11', pip={
    'gtfs-kit': '5.0.2', 'geopandas': '0.14.4',
    'pandas': '1.5.3', 'numpy': '1.23.2'
})
def current_stops(data=bauplan.Model("route_snapshots")):
    stops = read_gtfs_feed(data).stops
    assert stops is not None
    return stops[["stop_id", "stop_lat", "stop_lon"]]
