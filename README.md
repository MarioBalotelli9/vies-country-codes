# VIES COUNTRY CODES

Get updated European Union country codes in the ISO 3166-1 alpha-2 standard, recognized by the VAT Information Exchange System (VIES).

## Installation

* Clone this repository

* Create a virtual environment and activate it

```shell
cd vies-country-codes/
python3 -m venv myenv
source myenv/bin/activate
```

* Install dependencies

```shell
pip3 install -r requirements.txt
```

* Get the list of codes

```python3
from vies_country_codes import get_iso_codes

codes_list = get_iso_codes()
```

* or just run the sample code

```shell
python3 example.py
```