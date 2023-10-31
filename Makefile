all: kube_setup images kube

images: dice_roll

# Setup images
dice_roll:
	cd non_communicating/dice_roll; ${MAKE}

greetings:
	cd non_communicating/greetings; ${MAKE}

timestamp:
	cd non_communicating/timestamp; ${MAKE}

# Initial kubernetes setup
kube_setup:
	minikube start --driver hyperkit
	minikube addons enable ingress

# Apply kubernetes changes
kube:
	cd kubernetes; kubectl apply -f final.yml
