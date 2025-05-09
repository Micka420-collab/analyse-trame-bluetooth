# 🔍 Bluetooth Frame Analysis

This repository contains a Python script designed to extract information from Bluetooth exchanges between a computer and a **Bluetooth phone – Unknown file format**.

## 🎯 Objective

> From a binary Bluetooth file containing communication between a computer and a phone, the goal is to identify:
>
> * the phone’s MAC address
> * the device name
> * and submit the following SHA1 hash:
>
> ```
> SHA1("MAC_ADDRESS" + "PhoneName")
> ```

## 🧰 Repository Contents

* `analyse_trame_bluetooth.py`: main script to extract information and generate the hash.

## ⚙️ Usage

1. Place the `chxx.bin` (Bluetooth binary file) in the same directory as the script.
2. Edit the MAC address in the script if needed (`adresse_mac = "..."`).
3. Run the script:

```bash
python3 analyse_trame_bluetooth.py
```

4. The script will display all extracted device names and their corresponding SHA1 hashes.

## ✅ Example

Input:

```
MAC = 0C:B3:19:B9:4F:C6
Name = GT-S7390G
```

Output:

```
SHA1(0C:B3:19:B9:4F:C6GT-S7390G) = c1d0349c153ed96fe2fadf44e880aef9e69c122b
```

## 🛠 Dependencies

No external dependencies. Works with Python ≥ 3.6.

**Author**: 🧠 By Micka Delcato| Wireshark, Python, and a bit of patience.
