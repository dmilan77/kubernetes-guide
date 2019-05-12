### Install Kubernetes cluster:

### 1 Master + 2 Worker Nodes

### All Nodes
### ---------
### Get the Docker gpg key:
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

### Add the Docker repository
`sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`

### Get the Kubernetes gpg key
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

### Add the Kubernetes repository
cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

### Update your packages
sudo apt-get update

### Install Docker, kubelet, kubeadm, and kubectl
sudo apt-get install -y docker-ce=18.06.1~ce~3-0~ubuntu kubelet=1.13.5-00 kubeadm=1.13.5-00 kubectl=1.13.5-00

### Hold them at the current version
sudo apt-mark hold docker-ce kubelet kubeadm kubectl

### Add the iptables rule to sysctl.conf
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf

### Enable iptables immediately:
sudo sysctl -p



### Only on Mater Node
### Do not run on Worker nodes
### Initialize the cluster 
### pod-network-cidr
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

### Set up local kubeconfig:
### To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

### Apply Flannel CNI network overlay
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml


### Only on Worker Nodes
### Do not run on Master node

### You can now join any number of machines by running the following on each node as root:

sudo kubeadm join 172.31.116.211:6443 --token gpf68h.mppk7tdx8ddxydcx --discovery-token-ca-cert-hash sha256:3602282b6dbb51abd77b445d0fac9a079b1d82a8e3cdf18de1438fd5bfba2d79

