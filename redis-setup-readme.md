"""# Setup Redis on Windows via WSL2

This guide outlines the step-by-step process to set up a robust Redis environment on Windows using the Windows Subsystem for Linux (WSL2).

---

## Prerequisites
- Windows 10 or 11
- Administrator access
- Internet connection

---

## Step 1: Initial WSL Installation
Open **PowerShell** as an **Administrator** and run:

```powershell
wsl --install
```
> **Note:** If you already have WSL installed, you can skip this. A system restart may be required after this step.
---

## Step 2: Enable WSL Features & Hypervisor

Sometimes the GUI fails to deploy all components. We force-enable them via the terminal.

### 1. Force-Enable Features

Open **PowerShell (Admin)** and run these commands one by one:

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

```

### 2. Set Hypervisor to Auto-Launch

If the hypervisor layer is missing, WSL will fail to execute. Run:

```powershell
bcdedit /set hypervisorlaunchtype auto

```

**⚠️ RESTART YOUR COMPUTER NOW.** This is mandatory to register the services.

---

## Step 3: Verify Windows Features

Ensure the software platform is active within the Windows UI.

1. Click the **Start** menu, type `Turn Windows features on or off`, and hit **Enter**.
2. Locate and check the boxes for:
* [x] **Virtual Machine Platform**
* [x] **Windows Subsystem for Linux**


3. Click **OK**. (Do not restart yet; we will check BIOS next).

---

## Step 4: Enable Hardware Virtualization (BIOS)

The CPU must have virtualization enabled at the hardware level.

1. **Enter BIOS:** Restart your PC and repeatedly tap the BIOS key (usually `F1`, `F2`, `F10`, `Del`, or `Esc`).
2. **Locate Virtualization:** Look under **Advanced**, **Configuration**, or **Security** tabs.
3. **Enable Setting:** Find one of the following and set it to **Enabled**:
* Intel Virtualization Technology (Intel VT-x)
* AMD-V (or SVM Mode)


4. **Save and Exit:** Press `F10` to save and reboot into Windows.

---

## Step 5: Install Ubuntu & Redis

### 1. Setup Linux Distro

Open the **Ubuntu** app from your Start menu. Wait for the installation to finish, then create your **username** and **password**.

### 2. Install Redis

Inside the Ubuntu terminal, run the following to add the official repository and install Redis:

```bash
# Add Redis GPG key and repository
curl -fsSL [https://packages.redis.io/gpg](https://packages.redis.io/gpg) | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] [https://packages.redis.io/deb](https://packages.redis.io/deb) $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

# Update and Install
sudo apt-get update
sudo apt-get install redis -y

```

### 3. Start and Test Redis

* **Start the Service:**
```bash
sudo service redis-server start

```


* **Verify Connection:**
```bash
redis-cli

```


* **Ping Test:** Type `ping`. If it responds with `PONG`, Redis is running correctly!

---

## Troubleshooting: Memory Overcommit

If you see an error regarding `vm.overcommit_memory=1`:

1. Run: `sudo sysctl vm.overcommit_memory=1`
2. To make it permanent, add `vm.overcommit_memory = 1` to the end of `/etc/sysctl.conf`:
```bash
sudo nano /etc/sysctl.conf
# Add the line at the bottom, then Save (Ctrl+O) and Exit (Ctrl+X)
sudo sysctl -p