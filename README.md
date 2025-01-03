# 2023 | Project Community Spider - Places Data Engineering

Hi and welcome to the Community Spider of 2023. This project is a new updated version of 2021-2022 | [Places Spider](https://gitlab.com/geo-spider/places-spider).
Large companies, government organizations often add contact information on their own web resources so that clients can easily find the nearest office branches or service points.
The data can contain only address information without georeferencing, but in most cases, for the convenience of users, an interactive map is created with the display of objects in the form of points.

Our goal is to obtain data on the location of objects of a particular company with the maximum amount of related attributive information (phone number, work schedule, etc.).

## Project links
* Guideline: [Knowledge base](https://twilty.com/app/viewer/962ca15e-2e9c-4d40-910b-4fb381547ab0).
* Trello: [Kanban board](https://trello.com/invite/b/wDuQECbB/ATTI8de3b06bd30f98006fbcad848f8d741e84BDCF17/global-data-engineering-places).
* Community Tutorials: [`COMMUNITY_TUTORIALS.md`](docs/COMMUNITY_TUTORIALS.md)

## User-facing deps
* Framework: Scrapy - [Scrapy Docs](https://scrapy.org/).
* Help packages:
    * BeautifulSoup - [bs4 docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
    * Selenium - [Selenium Docs](https://selenium-python.readthedocs.io/index.html).


## Installation
```bash
# install pipenv tool
pip install pipenv

# install dependencies
pipenv install

# run tests
pipenv run pytest

# run spider
pipenv run scrapy crawl {spider_name_dpa} -o {spider_name_dpa}.geojson --logfile={spider_name_dpa_error}.log -s LOGSTATS_FILE={spider_name_dpa_stats}.log 
```

# DATA FORMAT

## Identifier

Each GeoJSON feature has an `id` field. The ID is a hash based on the `ref` and `@spider` fields and should be consistent between builds. You might use this to determine if new objects show up or disappear between builds.

## Geometry

In most cases, the feature will include a `geometry` field following [the GeoJSON spec](https://tools.ietf.org/html/rfc7946#section-3.1). There are some spiders that aren't able to recover a position from the venue's website. In those cases, the geometry is set to `null` and only the properties are included.

Although it's not supported at the time of this writing, we hope to include a geocoding step in the pipeline so that these feature will get a position added.

## Properties

Each GeoJSON feature will have a `properties` object with the following keys:

| Name | Required? | Description |
|---|---|---|
| `ref`           | Yes | A unique identifier for this feature inside this spider. The code that generates the output will remove duplicates based on the value of this key.
| `@spider`       | Yes | Generated automatically
| `chain_id`      | Yes | Static attribute which can be taken from trello card. Must be defined like = `self.spider_chain_id`
| `chain_name`    | Yes | Static attribute. Must be defined like = `self.brand_name`
| `addr_full`     | No  | Usually this follows the format of street, city, province, postcode address. This field might exist instead of the other address-related fields, especially if the spider can't reliably extract the individual parts of the address.
| `housenumber`   | No  | The house number part of the address.
| `street`        | No  | The street name.
| `city`          | No  | The city part of the address.
| `state`         | No  | The state or province part of the address.
| `postcode`      | No  | The postcode part of the address.
| `country`       | No  | The country part of the address.
| `phone`         | No  | The telephone number for the venue. Note that this is usually pulled from a website assuming local visitors, so it probably doesn't include the country code.
| `website`       | Yes | Static URL of the website from which you collect data. Example https://www.mcdonalds.rs/
| `store_url`     | No  | Dynamic URL of the page on the website. Usually we add this attribute when website renders information about different places on a different pages.
| `opening_hours` | No  | [OpenStreetMap's `opening_hours` format](https://wiki.openstreetmap.org/wiki/Key:opening_hours#Examples).
| `lat`           | No  | Latitude
| `lon`           | No  | Longitude