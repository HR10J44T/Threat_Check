
# 🔥 Real-Time Cybersecurity Threat Monitoring Dashboard

A **hacker-style**, real-time **terminal dashboard** for Kali Linux that monitors:

- 🛡️ Intrusion Attempts (simulated)
- 🦠 Malware Detections (simulated)
- 💀 Ransomware Alerts (simulated)
- 🎯 Phishing Attempts (simulated)
- 👤 Suspicious Logins (simulated)
- 🔀 Lateral Movement Detection (simulated)
- ⚠️ **Failed `sudo` Login Attempts** (real from your system logs)

This is a **fun, educational** dashboard to give your Kali terminal that “SOC Analyst / Hacker” vibe while you monitor activity.

---

## 📸 Demo Screenshot

> _(Imagine this in your terminal with animated colors!)_

```

════════════════════════════════════════════════════════════
REAL-TIME CYBERSECURITY THREAT MONITORING DASHBOARD
════════════════════════════════════════════════════════════
Time: 2025-08-12 14:23:56

\[!] Intrusion Attempts:      2
\[!] Malware Detections:      0
\[!] Ransomware Alerts:       1
\[!] Phishing Attempts:       4
\[!] Suspicious Logins:       1
\[!] Lateral Movement:        0
\[!] Failed sudo Attempts:    3

████████████████████████████████████████████████████████████
Monitoring in progress... Press CTRL+C to stop
████████████████████████████████████████████████████████████

````

---

## 🚀 Features

✅ **Continuous scanning** every 2 seconds  
✅ **Color-coded alerts** for quick reading  
✅ **Real sudo failure detection** via `journalctl`  
✅ Works in **Kali Linux & Debian-based systems**  
✅ No external dependencies except `colorama`  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone or Download
```bash
git clone https://github.com/yourusername/threat-monitor-dashboard.git
cd threat-monitor-dashboard
````

Or simply create a new file and paste the provided script.

---

### 2️⃣ Install Python Requirements

We only need `colorama` for colorful output:

```bash
pip install colorama
```

---

### 3️⃣ Give Execute Permissions

```bash
chmod +x hacker_dashboard.py
```

---

### 4️⃣ Run the Dashboard

> You must use `sudo` to read failed login logs.

```bash
sudo python3 hacker_dashboard.py
```

---

## 🧩 How It Works

* **Simulated Threat Data**: Generates random values for intrusion, malware, phishing, ransomware, suspicious logins, and lateral movements for a realistic “busy” look.
* **Real Sudo Failures**: Uses:

```bash
journalctl _COMM=sudo | grep 'authentication failure'
```

to count failed attempts.

* **Continuous Refresh**: Updates every 2 seconds, clearing the terminal for a smooth “live feed” effect.

---

## 🎯 For Beginners

If you’re new to Kali Linux:

1. Open a terminal
2. Paste the commands above one-by-one
3. Watch the live dashboard update!
4. Try typing `sudo wrongpassword` in another terminal to see the **Failed sudo Attempts** counter go up.

---

## ⚠️ Disclaimer

This script is **for educational & demonstration purposes only**.
It is **NOT** a replacement for a real SIEM/IDS/IPS solution.
Use responsibly.

---

## 📢 Next Steps (Optional)

You can make it **truly real-time** by connecting it to:

* `fail2ban` logs for intrusion detection
* `clamav` for malware scan reports
* `suricata` or `snort` for network IDS alerts

---

**💻 Author:** *Uday aka HR10J44T*
**🗓️ Last Updated:** August 2025

```

---

If you want, I can now make an **animated GIF terminal demo** that you can embed into this README so it moves like a real hacker dashboard. That will make it way more eye-catching on GitHub.
```
