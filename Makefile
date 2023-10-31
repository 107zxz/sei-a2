all: kube_setup images kube

images: dice_roll greetings timestamp input_validate calculate format_output

# Setup images
dice_roll:
	cd non_communicating/dice_roll && ${MAKE}

greetings:
	cd non_communicating/greetings && ${MAKE}

timestamp:
	cd non_communicating/timestamp && ${MAKE}


input_validate:
	cd communicating/input_validate && ${MAKE}

calculate:
	cd communicating/calculate && ${MAKE}

format_output:
	cd communicating/format_output && ${MAKE}

# Initial kubernetes setup
kube_setup:
	minikube start
	minikube addons enable ingress

kill_companion_kube:
	minikube delete


# Apply kubernetes changes
kube:
	cd kubernetes && kubectl apply -f final.yml
unkube:
	cd kubernetes && kubectl delete -f final.yml
rekube: unkube kube


# Add host
addhost:
	echo Adding host kube.info to /etc/hosts
