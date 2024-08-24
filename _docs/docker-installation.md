# **Docker Installation Guide**

This guide outlines the steps to install Docker on your system.

## **Prerequisites**

Before installing Docker, ensure that your system meets the following requirements:
- A supported operating system. Docker supports a variety of operating systems including Linux, macOS, and Windows. Refer to the [official documentation](https://docs.docker.com/get-docker/) for the full list of supported platforms.
- Sufficient disk space to accommodate Docker images and containers.

## **Installation Instructions**

### **Linux**

1. Update the package index:
    ```bash
    sudo apt-get update
    ```

2. Install necessary dependencies to add Docker repository:
    ```bash
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    ```

3. Add the official Docker GPG key:
    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

4. Add the Docker repository to APT sources:
    ```bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```

5. Update the package index again:
    ```bash
    sudo apt-get update
    ```

6. Install Docker:
    ```bash
    sudo apt-get install docker-ce
    ```

7. Verify that Docker is installed correctly:
    ```bash
    docker --version
    ```

### **macOS**

1. Download the Docker Desktop installer from the [official Docker website](https://docs.docker.com/docker-for-mac/install/).

2. Double-click the downloaded `.dmg` file to start the installation process.

3. Drag the Docker icon to the Applications folder.

4. Open Docker from the Applications folder to start Docker Desktop.

5. Verify that Docker is installed correctly by clicking on the Docker icon in the menu bar and selecting "About Docker Desktop".

### **Windows**

1. Download the Docker Desktop installer from the [official Docker website](https://docs.docker.com/docker-for-windows/install/).

2. Double-click the downloaded `.exe` file to start the installation process.

3. Follow the prompts in the installer to complete the installation.

4. Once installed, Docker Desktop will start automatically.

5. Verify that Docker is installed correctly by opening PowerShell or Command Prompt and running:
    ```bash
    docker --version
    ```

## **Post-installation Steps**

After installing Docker, you may need to perform additional configuration steps depending on your operating system. Refer to the [official documentation](https://docs.docker.com/get-docker/) for post-installation instructions specific to your platform.
