# portsort

Small helper that takes a flat list of `IP:port` pairs and splits it into one file per
port, with the IPs in each file sorted numerically. Handy for turning raw scan output into
per-service target lists (e.g. every host with 445 open in `port445.txt`).

## Requirements

- Python 3 (standard library only)

## Usage

```bash
python3 portsort.py
```

You'll be prompted for the path to an input file (tab-completion is enabled). The input is
one `IP:port` per line:

```
10.0.0.5:445
10.0.0.9:80
10.0.0.5:80
10.0.0.20:445
```

Output is written to a `ports/` directory next to where you run it, one file per port with
IPs sorted low to high:

```
ports/port445.txt   ->  10.0.0.5, 10.0.0.20
ports/port80.txt    ->  10.0.0.5, 10.0.0.9
```
