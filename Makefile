PROJECT_NAME := mobiflix-API
# File names
DOCKER_REL_COMPOSE_FILE := docker-compose.yml

# Docker compose project names
DOCKER_REL_PROJECT := "$(PROJECT_NAME)rel"

.PHONY: help


## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo "${YELLOW} make ${RESET} ${GREEN}<target> [options]${RESET}"
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
    	message = match(lastLine, /^## (.*)/); \
		if (message) { \
			command = substr($$1, 0, index($$1, ":")-1); \
			message = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW_S}%-$(TARGET_MAX_CHAR_NUM)s${RESET} %s\n", command, message; \
		} \
	} \
    { lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''


## Start the backend application
start:
	@ echo "${YELLOW}====> Building mobiflix backend image.${WHITE}"
	@ docker-compose -f $(DOCKER_REL_COMPOSE_FILE) build --no-cache backend
	@ echo "${GREEN}====> Image built. Image name is \"mobiflix\"${WHITE}"
	@ echo "${YELLOW}====> Starting the application${WHITE}"
	@ docker-compose -p mobi -f $(DOCKER_REL_COMPOSE_FILE) up --force-recreate -d backend
	@ echo "${YELLOW}====> Application is running at \"http://0.0.0.0:8000/\"${WHITE}"
	@ open http://0.0.0.0:8000/docs/


## Stop the backend application
stop:
	@ echo "${YELLOW}====> Stopping backend and database containers if they are running${WHITE}"
	@ docker-compose -p mobi -f $(DOCKER_REL_COMPOSE_FILE) stop
	@ echo "${YELLOW}====> Removing running containers for the backend if stopped containers exist${WHITE}"
	@ docker-compose -p mobi -f $(DOCKER_REL_COMPOSE_FILE) rm -f
	@ echo "${YELLOW}====> Removing image for the backend application${WHITE}"
	@ docker images -q --filter "reference=mobiflix" | xargs -I ARGS docker image rm ARGS
	@ echo "${GREEN}====> Container and image removed.${WHITE}"



## Build project image
release:
	${INFO} "Building required container image for the application"
	@ echo " "
	@ docker-compose -p $(DOCKER_REL_PROJECT) -f $(DOCKER_REL_COMPOSE_FILE) build app
	@ docker-compose -p $(DOCKER_REL_PROJECT) -f $(DOCKER_REL_COMPOSE_FILE) run -d app


  # COLORS
GREEN  := `tput setaf 2`
YELLOW := `tput setaf 3`
WHITE  := `tput setaf 7`
YELLOW_S := $(shell tput -Txterm setaf 3)
NC := "\e[0m"
RESET  := $(shell tput -Txterm sgr0)
# Shell Functions
INFO := @bash -c 'printf $(YELLOW); echo "===> $$1"; printf $(NC)' SOME_VALUE
SUCCESS := @bash -c 'printf $(GREEN); echo "===> $$1"; printf $(NC)' SOME_VALUE
