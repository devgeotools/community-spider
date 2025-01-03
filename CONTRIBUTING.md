# Conventions

1. Script file name should be same as "name" attribute inside class.
2. If script collects data for one country, country ISO-3 code should be reflected in script file name.
3. Each script file name should end with "_dpa" as identifier of team name.

## Static spatial files

1. Files with location information for spatial HTTP requests should be located in [searchable_points](https://gitlab.com/geo-spider/community-spider/-/tree/main/locations/searchable_points?ref_type=heads)
2. File name should be similar to spider name. For example `shell_hun_dpa.csv`.
3. No dependency on file format. Popluar files formats: `csv`, `geojson`.
