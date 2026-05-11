# JSON Module Quick Notes

## Important
- Python has NO separate JSON datatype
- JSON in Python is usually just a string (`str`)

---

## JSON String → Python Object

```python
import json

json_data = '{"name":"Rounak"}'

data = json.loads(json_data)
```

`loads()` converts:
```text
JSON string → Python object
```

---

## Python Object → JSON String

```python
import json

data = {"name": "Rounak"}

json_data = json.dumps(data)
```

`dumps()` converts:
```text
Python object → JSON string
```

---

## File Functions

| Function | Purpose |
|---|---|
| `dump()` | Write JSON to file |
| `load()` | Read JSON from file |

---

## Memory Trick

```text
loads  -> string to object
dumps  -> object to string
```

---

## Type Mapping

| Python | JSON |
|---|---|
| dict | object |
| list | array |
| str | string |
| int/float | number |
| True | true |
| False | false |
| None | null |