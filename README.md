============================================
Readme
============================================

docker build -t arindambanerjee/footapp:v1 foot-app/

kubectl apply -f footapp-namespace.yml

kubectl apply -f service-account.yml

kubectl apply -f secret.yml
kubectl create secret generic footapp-secret --from-literal MY_SECRET='My Super Secret' -n footapp

kubectl apply -f configmap.yml

kubectl apply -f pod-security/

kubectl apply -f secret-reader/

kubectl apply -f deploy-footballapp.yml