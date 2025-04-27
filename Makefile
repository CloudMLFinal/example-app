build:
	docker build -t cloudml-app .

run:
    docker run -d --name cloudml-app -p 5000:5000 cloudml-app

test:
	python -m unittest test_app.py

remove:
	docker stop cloudml-app
	docker rm cloudml-app