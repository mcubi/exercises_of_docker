# Práctica: Fiesta Meter — Flask + Gunicorn + Nginx
---
## 1 — App's Dockerfile (Gunicorn)

<img width="677" height="377" alt="image" src="https://github.com/user-attachments/assets/ae3999a2-22c3-42de-81ea-b02cd6f39cef" />

---

## 2 — Building the image

```docker build -t viaje-estudios .```

---

## 3 — Creating the network

```
docker network create webnet
```
---

## 4 — Flask execute (Gunicorn)

```
docker run -d --name fiesta_app --network webnet viaje-estudios
```
## To see logs;

```
docker logs fiesta_app
```
```
[INFO] Listening at: http://0.0.0.0:8000
[INFO] Booting worker with pid: 6
```

---

## 5 — Nginx server: proxy config

<img width="800" height="382" alt="image" src="https://github.com/user-attachments/assets/6403992a-bf65-4bc0-a112-808bb027183a" />


## Nginx running:

```
docker run -d --name nginx_proxy   --network webnet   -p 8080:80   -v ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro   nginx:1.27-alpine
```

---

## 6 — Testing

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f2610308-579d-4c7e-909c-3c5d43e618db" />

<img width="1919" height="1076" alt="image" src="https://github.com/user-attachments/assets/7b98dc72-1fe3-4301-993e-9982ac0ebfbb" />


---

## Why Flask doesn't expose itself directly?

First of all, web servers like Nginx or Apache does not run Python commands by default, so the existence of WSGI server actors is necessary to have compatibility.
Also, frameworks like Flask are not designed for production and high traffic. So Flask expose the features, Gunicorn acts as WSGI server providing compatibility and efficiency, and
Nginx acts as 'reverse proxy' so it can receive the requests and tasks, providing performance, scalability and improving security
