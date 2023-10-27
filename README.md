# BEM VINDO EU.A3

Nesse Lab falaremos um pouco sobre como montar um DataWarehouse/LakeHouse para estudos!

Na pasta bases estão presentes os arquivos .csv que iremos utilizar
Na pasta composer_a3 está o arquivo docker-compose.yaml, necessário para subir o container Docker
Na pasta conf está o arquivo .env utilizado como variaveis de ambiente
Na pasta data encontram-se os volumes utilizados pelo container
Na pasta scritps estão os scripts que iremos utilizar

## CONFIGURAÇÕES INICIAIS

### Instalação GIT
https://git-scm.com/download/win

git config --global user.name USER
git config --global user.email EMAIL

### Instalação Chocolatey
https://chocolatey.org/install
PowerShell as ADMIN: Set-ExecutionPolicy AllSigned
PowerShell as ADMIN: Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

### ATENÇÂO 
Quando instalar um pacote pelo Choco, a seguinte mensagem será exibida Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint):
Nesse caso, digitar A e pressionar Enter para permitir que todos os scripts de instalações sejam executados

#### Instalação Kind Docker
Na Windows VM:
	Criar a máquina, executar o Power Shell como ADMIN e Set-VMProcessor -VMName <Nome VM>-ExposeVirtualizationExtensions $true
	Iniciar a máquina, ir em Ativar ou Desativar recursos do Windows, ativar HyperV. Reiniciar a Maquina

PowerShell as ADMIN: wsl --install -d ubuntu
PowerShell as ADMIN: choco install kind

### Instalação Python
choco install python --version=3.9.12 ou https://www.python.org/ftp/python/3.9.12/python-3.9.12-amd64.exe

### Repo LakeHouse
https://github.com/guilhermesb17/lakehouse_a3 

