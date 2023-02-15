# Test loadBalancer per node

## Get venv

```bash
python3 -m venv dev
source dev/bin/activate
```

## Install requirements.txt

```bash
pip install -r requirements.txt
```

## Run code

```bash
python3 test.py
╒══════════════════╤═══════════╕
│   Request Number │   Threads │
╞══════════════════╪═══════════╡
│             1000 │        10 │
╘══════════════════╧═══════════╛
╒══════════╤══════════╤══════════╤══════════╕
│   Node 1 │   Node 2 │   Node 3 │   Node 4 │
╞══════════╪══════════╪══════════╪══════════╡
│      136 │      335 │      314 │      215 │
╘══════════╧══════════╧══════════╧══════════╛
```
